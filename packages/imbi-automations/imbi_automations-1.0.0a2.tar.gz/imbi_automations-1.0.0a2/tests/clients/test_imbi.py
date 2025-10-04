import http
import typing
import unittest

import httpx

from imbi_automations import models
from imbi_automations.clients import http as ia_http
from imbi_automations.clients import imbi
from tests import base


def create_mock_project_data(
    project_id: int,
    name: str,
    namespace_slug: str,
    project_type_slug: str,
    slug: str,
    description: str | None = None,
    links: dict[str, str] | None = None,
    identifiers: dict[str, str] | None = None,
    facts: dict[str, str] | None = None,
) -> dict[str, typing.Any]:
    """Helper function to create mock Imbi project data."""
    return {
        '_source': {
            'id': project_id,
            'name': name,
            'description': description,
            'namespace': namespace_slug.replace('-', ' ').title(),
            'namespace_slug': namespace_slug,
            'project_type': project_type_slug.upper(),
            'project_type_slug': project_type_slug,
            'slug': slug,
            'dependencies': None,
            'environments': None,
            'facts': facts,
            'identifiers': identifiers,
            'links': links,
            'project_score': None,
            'urls': None,
        }
    }


class TestImbiClient(base.AsyncTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.config = models.ImbiConfiguration(
            api_key='uuid-test-token', hostname='imbi.example.com'
        )
        self.instance = imbi.Imbi(self.config, self.http_client_transport)

    async def test_imbi_init(self) -> None:
        """Test Imbi client initialization."""
        client = imbi.Imbi(self.config)

        self.assertEqual(client.base_url, 'https://imbi.example.com')
        # Check that the Private-Token header is set
        headers = client.http_client.headers
        self.assertIn('Private-Token', headers)
        self.assertEqual(headers['Private-Token'], 'uuid-test-token')

    async def test_imbi_init_with_custom_transport(self) -> None:
        """Test Imbi client initialization with custom transport."""
        transport = httpx.MockTransport(lambda request: httpx.Response(200))
        client = imbi.Imbi(self.config, transport)

        self.assertEqual(client.base_url, 'https://imbi.example.com')
        self.assertIsInstance(
            client.http_client._transport, httpx.MockTransport
        )

    async def test_get_project_success(self) -> None:
        """Test successful project retrieval by ID."""
        # Mock OpenSearch response
        opensearch_data = {
            'hits': {
                'hits': [
                    create_mock_project_data(
                        123,
                        'Test Project',
                        'testorg',
                        'api',
                        'test-project',
                        description='A test project',
                        links={
                            'GitHub Repository': 'https://github.com/testorg/test-project'
                        },
                        identifiers={'github': '789'},
                        facts={'language': 'Python'},
                    )
                ]
            }
        }

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=opensearch_data,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance.get_project(123)

        self.assertIsInstance(result, models.ImbiProject)
        self.assertEqual(result.id, 123)
        self.assertEqual(result.name, 'Test Project')
        self.assertEqual(result.namespace_slug, 'testorg')
        self.assertIn(
            'https://imbi.example.com/ui/projects/123', result.imbi_url
        )

    async def test_get_project_not_found(self) -> None:
        """Test project retrieval when project doesn't exist."""
        opensearch_data = {'hits': {'hits': []}}

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=opensearch_data,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance.get_project(999)

        self.assertIsNone(result)

    async def test_get_projects_by_type_success(self) -> None:
        """Test successful projects retrieval by type."""
        opensearch_data = {
            'hits': {
                'hits': [
                    create_mock_project_data(
                        111,
                        'API Project 1',
                        'team1',
                        'api',
                        'api-project-1',
                        description='First API project',
                    ),
                    create_mock_project_data(
                        222,
                        'API Project 2',
                        'team2',
                        'api',
                        'api-project-2',
                        description='Second API project',
                    ),
                ]
            }
        }

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=opensearch_data,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance.get_projects_by_type('api')

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], models.ImbiProject)
        self.assertEqual(result[0].slug, 'api-project-1')  # Sorted by slug
        self.assertEqual(result[1].slug, 'api-project-2')

    async def test_get_projects_by_type_empty(self) -> None:
        """Test projects retrieval by type with no results."""
        opensearch_data = {'hits': {'hits': []}}

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=opensearch_data,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance.get_projects_by_type('nonexistent')

        self.assertEqual(len(result), 0)

    async def test_get_all_projects_success(self) -> None:
        """Test successful retrieval of all projects."""
        opensearch_data = {
            'hits': {
                'hits': [
                    create_mock_project_data(
                        333,
                        'All Projects Test',
                        'testns',
                        'library',
                        'all-projects-test',
                        description='Test for all projects',
                    )
                ]
            }
        }

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=opensearch_data,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance.get_all_projects()

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], models.ImbiProject)
        self.assertEqual(result[0].id, 333)
        self.assertEqual(result[0].slug, 'all-projects-test')

    async def test_search_projects_by_github_url_success(self) -> None:
        """Test successful search for projects by GitHub URL."""
        opensearch_data = {
            'hits': {
                'hits': [
                    create_mock_project_data(
                        444,
                        'GitHub Linked Project',
                        'github-team',
                        'api',
                        'github-linked-project',
                        description='Project with GitHub link',
                        links={
                            'GitHub Repository': 'https://github.com/testorg/test-repo'
                        },
                    )
                ]
            }
        }

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=opensearch_data,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance.search_projects_by_github_url(
            'https://github.com/testorg/test-repo'
        )

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], models.ImbiProject)
        self.assertEqual(result[0].id, 444)
        self.assertEqual(result[0].slug, 'github-linked-project')

    async def test_search_projects_by_github_url_not_found(self) -> None:
        """Test search for projects by GitHub URL with no results."""
        opensearch_data = {'hits': {'hits': []}}

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=opensearch_data,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance.search_projects_by_github_url(
            'https://github.com/nonexistent/repo'
        )

        self.assertEqual(len(result), 0)

    async def test_opensearch_projects_request_error(self) -> None:
        """Test OpenSearch request error handling."""
        self.http_client_side_effect = httpx.RequestError('Connection failed')

        result = await self.instance._opensearch_projects(
            {'query': {'match_all': {}}}
        )

        self.assertEqual(len(result), 0)

    async def test_opensearch_projects_http_error(self) -> None:
        """Test OpenSearch HTTP error handling."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.INTERNAL_SERVER_ERROR,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance._opensearch_projects(
            {'query': {'match_all': {}}}
        )

        self.assertEqual(len(result), 0)

    async def test_opensearch_projects_no_hits(self) -> None:
        """Test OpenSearch response with no hits structure."""
        opensearch_data = {'no_hits': 'data'}

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=opensearch_data,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance._opensearch_projects(
            {'query': {'match_all': {}}}
        )

        self.assertEqual(len(result), 0)

    async def test_opensearch_projects_empty_data(self) -> None:
        """Test OpenSearch response with empty data."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=None,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance._opensearch_projects(
            {'query': {'match_all': {}}}
        )

        self.assertEqual(len(result), 0)

    def test_search_project_id(self) -> None:
        """Test project ID search query construction."""
        result = self.instance._search_project_id(123)

        self.assertIn('query', result)
        self.assertEqual(
            result['query']['bool']['filter'][0]['term']['_id'], '123'
        )

    def test_search_project_type_slug(self) -> None:
        """Test project type slug search query construction."""
        result = self.instance._search_project_type_slug('api')

        self.assertIn('query', result)
        self.assertEqual(
            result['query']['bool']['must'][1]['term'][
                'project_type_slug.keyword'
            ],
            'api',
        )

    def test_opensearch_payload_structure(self) -> None:
        """Test OpenSearch payload structure."""
        result = self.instance._opensearch_payload()

        self.assertIn('_source', result)
        self.assertIn('exclude', result['_source'])
        self.assertIn('archived', result['_source']['exclude'])
        self.assertIn('query', result)

    def test_add_imbi_url(self) -> None:
        """Test adding Imbi URL to project data."""
        project_data = create_mock_project_data(
            555, 'URL Test Project', 'test', 'test', 'url-test-project'
        )

        result = self.instance._add_imbi_url(project_data)

        self.assertIsInstance(result, models.ImbiProject)
        self.assertEqual(result.id, 555)
        self.assertEqual(
            result.imbi_url, 'https://imbi.example.com/ui/projects/555'
        )

    async def test_opensearch_request_success(self) -> None:
        """Test successful OpenSearch request."""
        response_data = {'hits': {'hits': []}}

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=response_data,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        result = await self.instance._opensearch_request(
            '/opensearch/projects', {'query': {'match_all': {}}}
        )

        self.assertEqual(result, response_data)

    async def test_opensearch_request_http_error(self) -> None:
        """Test OpenSearch request with HTTP status error."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.BAD_REQUEST,
            content=b'Bad request',
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        with self.assertRaises(httpx.HTTPStatusError):
            await self.instance._opensearch_request(
                '/opensearch/projects', {'query': {'match_all': {}}}
            )

    async def test_get_projects_by_type_pagination(self) -> None:
        """Test projects by type with pagination."""
        # First page with full results
        first_page_data = {
            'hits': {
                'hits': [
                    create_mock_project_data(
                        i, f'Project {i}', 'team', 'api', f'project-{i:02d}'
                    )
                    for i in range(1, 101)  # 100 items (full page)
                ]
            }
        }

        # Second page with partial results
        second_page_data = {
            'hits': {
                'hits': [
                    create_mock_project_data(
                        101, 'Project 101', 'team', 'api', 'project-101'
                    )
                ]
            }
        }

        # Mock responses for pagination
        responses = [first_page_data, second_page_data]
        call_count = 0

        def mock_response(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            response_data = (
                responses[call_count]
                if call_count < len(responses)
                else {'hits': {'hits': []}}
            )
            call_count += 1
            return httpx.Response(
                http.HTTPStatus.OK, json=response_data, request=request
            )

        self.http_client_transport = httpx.MockTransport(mock_response)
        self.instance = imbi.Imbi(self.config, self.http_client_transport)

        result = await self.instance.get_projects_by_type('api')

        self.assertEqual(len(result), 101)  # 100 + 1 from two pages
        # Verify pagination worked by checking we got results from both pages
        project_ids = [p.id for p in result]
        self.assertIn(1, project_ids)  # From first page
        self.assertIn(101, project_ids)  # From second page

    async def test_imbi_inheritance_from_base_url_client(self) -> None:
        """Test that Imbi inherits properly from BaseURLHTTPClient."""
        self.assertIsInstance(self.instance, ia_http.BaseURLHTTPClient)
        self.assertTrue(hasattr(self.instance, 'get'))
        self.assertTrue(hasattr(self.instance, 'post'))
        self.assertTrue(hasattr(self.instance, 'put'))
        self.assertTrue(hasattr(self.instance, 'patch'))
        self.assertTrue(hasattr(self.instance, 'delete'))

    async def test_update_project_fact_success(self) -> None:
        """Test successful single project fact update."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/projects/123/facts'
            ),
        )

        # Should not raise any exception
        await self.instance.update_project_fact(
            123, fact_type_id=1, value='Python 3.12', skip_validations=True
        )

    async def test_update_project_fact_http_error(self) -> None:
        """Test project fact update with HTTP error."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.FORBIDDEN,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/projects/123/facts'
            ),
        )

        with self.assertRaises(httpx.HTTPError):
            await self.instance.update_project_fact(
                123, fact_type_id=1, value='Python 3.12', skip_validations=True
            )

    async def test_update_project_fact_different_types(self) -> None:
        """Test project fact update with different value types."""
        responses = [
            httpx.Response(
                http.HTTPStatus.OK,
                request=httpx.Request(
                    'POST', 'https://imbi.example.com/projects/123/facts'
                ),
            ),
            httpx.Response(
                http.HTTPStatus.OK,
                request=httpx.Request(
                    'POST', 'https://imbi.example.com/projects/123/facts'
                ),
            ),
            httpx.Response(
                http.HTTPStatus.OK,
                request=httpx.Request(
                    'POST', 'https://imbi.example.com/projects/123/facts'
                ),
            ),
            httpx.Response(
                http.HTTPStatus.OK,
                request=httpx.Request(
                    'POST', 'https://imbi.example.com/projects/123/facts'
                ),
            ),
        ]

        call_count = 0

        def mock_response(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            response = responses[call_count]
            call_count += 1
            return response

        self.http_client_transport = httpx.MockTransport(mock_response)
        self.instance = imbi.Imbi(self.config, self.http_client_transport)

        # Test different value types
        await self.instance.update_project_fact(
            123, fact_type_id=1, value='String value', skip_validations=True
        )
        await self.instance.update_project_fact(
            123, fact_type_id=2, value=42, skip_validations=True
        )
        await self.instance.update_project_fact(
            123, fact_type_id=3, value=95.5, skip_validations=True
        )
        await self.instance.update_project_fact(
            123, fact_type_id=4, value=True, skip_validations=True
        )

    async def test_update_project_facts_success(self) -> None:
        """Test successful multiple project facts update."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/projects/456/facts'
            ),
        )

        facts = [(1, 'Python 3.12'), (2, 98.5), (3, True)]

        # Should not raise any exception
        await self.instance.update_project_facts(456, facts)

    async def test_update_project_facts_http_error(self) -> None:
        """Test multiple project facts update with HTTP error."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.BAD_REQUEST,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/projects/456/facts'
            ),
        )

        facts = [(1, 'Invalid value')]

        with self.assertRaises(httpx.HTTPError):
            await self.instance.update_project_facts(456, facts)

    async def test_update_project_facts_empty_list(self) -> None:
        """Test multiple project facts update with empty facts list."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/projects/789/facts'
            ),
        )

        # Should not raise any exception
        await self.instance.update_project_facts(789, [])

    async def test_get_fact_types_success(self) -> None:
        """Test successful fact types retrieval."""
        fact_types_data = [
            {
                'id': 1,
                'name': 'Programming Language',
                'project_type_ids': [1, 2],
                'fact_type': 'enum',
                'data_type': 'string',
                'description': 'The programming language used',
            },
            {
                'id': 2,
                'name': 'Test Coverage',
                'project_type_ids': [1],
                'fact_type': 'range',
                'data_type': 'decimal',
                'description': 'Test coverage percentage',
            },
        ]

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=fact_types_data,
            request=httpx.Request(
                'GET', 'https://imbi.example.com/project-fact-types'
            ),
        )

        result = await self.instance.get_fact_types()

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], models.ImbiProjectFactType)
        self.assertEqual(result[0].name, 'Programming Language')
        self.assertEqual(result[1].name, 'Test Coverage')

    async def test_get_fact_type_id_by_name_found(self) -> None:
        """Test fact type ID lookup by name when found."""
        fact_types_data = [
            {
                'id': 5,
                'name': 'CI Pipeline Status',
                'project_type_ids': [1],
                'fact_type': 'enum',
                'data_type': 'string',
            }
        ]

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=fact_types_data,
            request=httpx.Request(
                'GET', 'https://imbi.example.com/project-fact-types'
            ),
        )

        result = await self.instance.get_fact_type_id_by_name(
            'CI Pipeline Status'
        )

        self.assertEqual(result, 5)

    async def test_get_fact_type_id_by_name_not_found(self) -> None:
        """Test fact type ID lookup by name when not found."""
        fact_types_data = []

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=fact_types_data,
            request=httpx.Request(
                'GET', 'https://imbi.example.com/project-fact-types'
            ),
        )

        result = await self.instance.get_fact_type_id_by_name(
            'Nonexistent Fact'
        )

        self.assertIsNone(result)

    async def test_update_project_fact_by_name_success(self) -> None:
        """Test updating project fact by name."""
        # Mock fact types response
        fact_types_data = [
            {
                'id': 10,
                'name': 'CI Pipeline Status',
                'project_type_ids': [1],
                'fact_type': 'enum',
                'data_type': 'string',
            }
        ]

        responses = [
            httpx.Response(
                http.HTTPStatus.OK,
                json=fact_types_data,
                request=httpx.Request(
                    'GET', 'https://imbi.example.com/project-fact-types'
                ),
            ),
            httpx.Response(
                http.HTTPStatus.OK,
                request=httpx.Request(
                    'POST', 'https://imbi.example.com/projects/123/facts'
                ),
            ),
        ]

        call_count = 0

        def mock_response(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            response = responses[call_count]
            call_count += 1
            return response

        self.http_client_transport = httpx.MockTransport(mock_response)
        self.instance = imbi.Imbi(self.config, self.http_client_transport)

        # Should not raise any exception
        await self.instance.update_project_fact(
            123,
            fact_name='CI Pipeline Status',
            value='pass',
            skip_validations=True,
        )

    async def test_update_project_fact_by_name_not_found(self) -> None:
        """Test updating project fact by name when fact type not found."""
        fact_types_data = []

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json=fact_types_data,
            request=httpx.Request(
                'GET', 'https://imbi.example.com/project-fact-types'
            ),
        )

        with self.assertRaises(ValueError) as cm:
            await self.instance.update_project_fact(
                123,
                fact_name='Nonexistent Fact',
                value='test',
                skip_validations=True,
            )

        self.assertIn('Fact type not found', str(cm.exception))

    async def test_update_project_fact_no_parameters(self) -> None:
        """Test updating project fact with no fact_name or fact_type_id."""
        with self.assertRaises(ValueError) as cm:
            await self.instance.update_project_fact(
                123, value='test', skip_validations=True
            )

        self.assertIn(
            'Either fact_name or fact_type_id must be provided',
            str(cm.exception),
        )

    async def test_update_project_fact_null_value(self) -> None:
        """Test updating project fact with 'null' value converts to None."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            request=httpx.Request(
                'POST', 'https://imbi.example.com/projects/123/facts'
            ),
        )

        # Should convert "null" to None and not raise exception
        await self.instance.update_project_fact(
            123, fact_type_id=1, value='null', skip_validations=True
        )

    async def test_update_github_identifier_new_value(self) -> None:
        """Test updating GitHub identifier with new value."""
        # Mock project data without existing identifier
        project_data = create_mock_project_data(
            123, 'Test Project', 'test', 'api', 'test-project'
        )

        # Mock responses: get project, then update identifier
        responses = [
            httpx.Response(
                http.HTTPStatus.OK,
                json={'hits': {'hits': [project_data]}},
                request=httpx.Request(
                    'POST', 'https://imbi.example.com/opensearch/projects'
                ),
            ),
            httpx.Response(
                http.HTTPStatus.OK,
                request=httpx.Request(
                    'POST', 'https://imbi.example.com/projects/123/identifiers'
                ),
            ),
        ]

        call_count = 0

        def mock_response(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            response = responses[call_count]
            call_count += 1
            return response

        self.http_client_transport = httpx.MockTransport(mock_response)
        self.instance = imbi.Imbi(self.config, self.http_client_transport)

        # Should not raise any exception
        await self.instance.update_github_identifier(123, 'github', 12345)

    async def test_update_github_identifier_same_value(self) -> None:
        """Test updating GitHub identifier with same value skips update."""
        # Mock project data with existing identifier
        project_data = create_mock_project_data(
            123,
            'Test Project',
            'test',
            'api',
            'test-project',
            identifiers={'github': '12345'},
        )

        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json={'hits': {'hits': [project_data]}},
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        # Should not make additional API call
        await self.instance.update_github_identifier(123, 'github', 12345)

    async def test_update_github_identifier_different_value(self) -> None:
        """Test updating GitHub identifier with different value."""
        # Mock project data with existing identifier
        project_data = create_mock_project_data(
            123,
            'Test Project',
            'test',
            'api',
            'test-project',
            identifiers={'github': '54321'},
        )

        # Mock responses: get project, then update identifier
        responses = [
            httpx.Response(
                http.HTTPStatus.OK,
                json={'hits': {'hits': [project_data]}},
                request=httpx.Request(
                    'POST', 'https://imbi.example.com/opensearch/projects'
                ),
            ),
            httpx.Response(
                http.HTTPStatus.OK,
                request=httpx.Request(
                    'POST', 'https://imbi.example.com/projects/123/identifiers'
                ),
            ),
        ]

        call_count = 0

        def mock_response(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            response = responses[call_count]
            call_count += 1
            return response

        self.http_client_transport = httpx.MockTransport(mock_response)
        self.instance = imbi.Imbi(self.config, self.http_client_transport)

        # Should update identifier
        await self.instance.update_github_identifier(123, 'github', 12345)

    async def test_update_github_identifier_project_not_found(self) -> None:
        """Test updating GitHub identifier when project doesn't exist."""
        self.http_client_side_effect = httpx.Response(
            http.HTTPStatus.OK,
            json={'hits': {'hits': []}},
            request=httpx.Request(
                'POST', 'https://imbi.example.com/opensearch/projects'
            ),
        )

        with self.assertRaises(ValueError) as cm:
            await self.instance.update_github_identifier(999, 'github', 12345)

        self.assertIn('Project not found: 999', str(cm.exception))


if __name__ == '__main__':
    unittest.main()
