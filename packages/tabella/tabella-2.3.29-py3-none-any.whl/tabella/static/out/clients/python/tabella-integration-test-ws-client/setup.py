from setuptools import setup

setup(
    name="tabella-integration-test-client",
    version="1.1.1",
    author="John Doe",
    author_email="email@website.test",
    description="Tabella Integration Test Python WS client.",
    packages=["tabella_integration_test_ws_client"],
    install_requires=[
        "jsonrpc2-pyclient>=5.2.0",
        "py-undefined>=0.1.5",
        "pydantic>=2.5.3"
    ],
)
