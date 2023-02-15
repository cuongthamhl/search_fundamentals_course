from flask import g, current_app
from opensearchpy import OpenSearch

# Create an OpenSearch client instance and put it into Flask shared space for use by the application
def get_opensearch():
    if 'opensearch' not in g:
        #### Step 4.a:
        # Implement a client connection to OpenSearch so that the rest of the application can communicate with OpenSearch
        g.opensearch = OpenSearch(
            hosts=[{'host': 'localhost', 'port': '9200'}],
            http_compress=True,  # enables gzip compression for request bodies
            auth = ('admin', 'admin'), # For testing only. Don't store credentials in code.
            # client_cert = client_cert_path,
            # client_key = client_key_path,
            use_ssl=True,
            verify_certs=False, # set to true if you have certs
            ssl_assert_hostname=False,
            ssl_show_warn=False,

        )

    return g.opensearch
