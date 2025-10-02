# PAYONE Commerce Platform Python SDK

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=PAYONE-GmbH_PCP-ServerSDK-python&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=PAYONE-GmbH_PCP-ServerSDK-python)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=PAYONE-GmbH_PCP-ServerSDK-python&metric=coverage)](https://sonarcloud.io/summary/new_code?id=PAYONE-GmbH_PCP-ServerSDK-python)
![PyPI - Version](https://img.shields.io/pypi/v/pcp_serversdk_python)
![PyPI - Downloads](https://img.shields.io/pypi/dw/pcp_serversdk_python)

Welcome to the Python SDK for the PAYONE Commerce Platform (api-version 1.35.0)! This repository contains a powerful, easy-to-use software development kit (SDK) designed to simplify the integration of online payment processing into your applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [General](#general)
  - [Authentication Token Retrieval](#authentication-token-retrieval)
  - [Error Handling](#error-handling)
  - [Client Side](#client-side)
  - [Apple Pay](#apple-pay)
- [Demo App](#demo-app)
- [Contributing](#contributing)
- [Releasing the library](#releasing-the-library)
  - [Preparing the Release](#preparing-the-release)
  - [Changelog Generation with Conventional Changelog](#changelog-generation-with-conventional-changelog)
  - [Merging the Release Branch](#merging-the-release-branch)
  - [GitHub Action for Release](#github-action-for-release)
  - [Optional: Creating a GitHub Release](#optional-creating-a-github-release)
- [License](#license)

## Features

- **Easy Integration**: Seamlessly integrate online payment processing into your application.
- **Secure Transactions**: Built with security best practices to ensure safe transactions.
- **Extensive Documentation**: Detailed documentation to help you get started quickly.
- **Open Source**: Fully open source and community-driven.

## Installation

```sh
python3 -m pip install "pcp_serversdk_python"
```

**[back to top](#table-of-contents)**

## Usage

### General

To use this SDK you need to construct a `CommunicatorConfiguration` which encapsulate everything needed to connect to the PAYONE Commerce Platform.

```python
from pcp_serversdk_python import CommunicatorConfiguration

API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']

communicatorConfiguration = CommunicatorConfiguration(API_KEY, API_SECRET, "https://api.preprod.commerce.payone.com")
```

With the configuration you can create an API client for each reource you want to interact with. For example to create a commerce case you can use the `CommerceCaseApiClient`.

```python
from pcp_serversdk_python import CommunicatorConfiguration, CheckoutApiClient

commerceCaseClient = CommerceCaseApiClient(communicatorConfiguration)
```

All payloads and reponses are availabe as python classes within the `pcp_serversdk_python.models` package. The serialization and deserialization is handled by the SDK internally. For example, to create an empty commerce case you can pass a `CreateCommerceCaseRequest` instance:

```python
createCommerceCaseRequest = CreateCommerceCaseRequest()
createCommerceCaseResponse = commerceCaseClient.createCommerceCaseRequest('merchant_id', createCommerceCaseRequest);
```

The models directly map to the API as described in [PAYONE Commerce Platform API Reference](https://docs.payone.com/pcp/commerce-platform-api). For an in depth example you can take a look at the [demo app](#demo-app).

### Authentication Token Retrieval

To interact with certain client-side SDKs (such as the credit card tokenizer), you need to generate a short-lived authentication JWT token for your merchant. This token can be retrieved using the SDK as follows:

```python
from pcp_serversdk_python.endpoints import AuthenticationApiClient

# ...
authentication_api_client = AuthenticationApiClient(communicatorConfiguration)
token = authentication_api_client.get_authentication_tokens(merchant_id)
print("JWT Token:", token.token)
print("Token ID:", token.id)
print("Created:", token.creationDate)
print("Expires:", token.expirationDate)
```

This token can then be used for secure operations such as initializing the credit card tokenizer or other client-side SDKs that require merchant authentication. The token is valid for a limited time (10 minutes) and should be handled securely.

**Note:** The `get_authentication_tokens` method requires a valid `merchant_id`. Optionally, you can provide an `X-Request-ID` header for tracing requests.

### HTTP Client Customization

The SDK allows you to customize the underlying HTTP client used for API requests. This enables you to configure timeouts, add custom headers, set up proxies, or implement other HTTP-level customizations. You can configure the HTTP client globally or for specific API clients.

#### Global HTTP Client Configuration

You can set a global HTTP client that will be used by all API clients created with a specific `CommunicatorConfiguration`:

```python
import httpx
from pcp_serversdk_python import CommunicatorConfiguration
from pcp_serversdk_python.endpoints import CommerceCaseApiClient

# Create a custom HTTP client with specific configuration
custom_http_client = httpx.AsyncClient(
    timeout=httpx.Timeout(30.0),  # 30 second timeout
    limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
    headers={"User-Agent": "MyApp/1.0"}
)

# Create configuration with custom HTTP client
config = CommunicatorConfiguration(
    api_key="your_api_key",
    api_secret="your_api_secret",
    host="https://api.preprod.commerce.payone.com",
    http_client=custom_http_client
)

# All API clients created with this config will use the custom HTTP client
commerce_case_client = CommerceCaseApiClient(config)
```

#### Client-Specific HTTP Client Configuration

You can also set a custom HTTP client for individual API clients, which will override the global configuration:

```python
import httpx
from pcp_serversdk_python import CommunicatorConfiguration
from pcp_serversdk_python.endpoints import CommerceCaseApiClient, CheckoutApiClient

# Create configuration (with or without global HTTP client)
config = CommunicatorConfiguration("api_key", "api_secret", "https://api.preprod.commerce.payone.com")

# Create API clients
commerce_case_client = CommerceCaseApiClient(config)
checkout_client = CheckoutApiClient(config)

# Set custom HTTP client only for the commerce case client
custom_client = httpx.AsyncClient(timeout=httpx.Timeout(60.0))
commerce_case_client.set_http_client(custom_client)

# commerce_case_client will use the custom client
# checkout_client will use the default client
```

#### Priority Order

The SDK follows this priority order when determining which HTTP client to use:

1. **Client-specific HTTP client** (set via `set_http_client()` on individual API clients)
2. **Global HTTP client** (set in `CommunicatorConfiguration`)
3. **Default HTTP client** (created automatically by the SDK)

#### Common Use Cases

**Setting Custom Timeouts:**
```python
# Create client with longer timeout for slow operations
slow_client = httpx.AsyncClient(timeout=httpx.Timeout(120.0))
config = CommunicatorConfiguration("key", "secret", "host", slow_client)
```

**Adding Custom Headers:**
```python
# Add custom headers to all requests
headers = {"X-Custom-Header": "value", "User-Agent": "MyApp/2.0"}
client = httpx.AsyncClient(headers=headers)
config = CommunicatorConfiguration("key", "secret", "host", client)
```

**Configuring Proxy:**
```python
# Configure HTTP client to use a proxy
proxy_client = httpx.AsyncClient(proxies="http://proxy.example.com:8080")
config = CommunicatorConfiguration("key", "secret", "host", proxy_client)
```

**Note:** When using custom HTTP clients, ensure they are properly configured for your use case and remember to close them when your application shuts down to free up resources.

### Error Handling

When making a request any client may throw a `ApiException`. There two subtypes of this exception:

- `ApiErrorReponseException`: This exception is thrown when the API returns an well-formed error response. The given errors are deserialized into `APIError` objects which are availble via the `getErrors()` method on the exception. They usually contain useful information about what is wrong in your request or the state of the resource.
- `ApiResponseRetrievalException`: This exception is a catch-all exception for any error that cannot be turned into a helpful error response. This includes malformed responses or unknown responses.

Network errors are not wrap, you can should handle the standard `IOExeption`.

### Client Side

For most [payment methods](https://docs.payone.com/pcp/commerce-platform-payment-methods) some information from the client is needed, e.g. payment information given by Apple when a payment via ApplePay suceeds. PAYONE provides client side SDKs which helps you interact the third party payment providers. You can find the SDKs under the [PAYONE GitHub organization](https://github.com/PAYONE-GmbH). Either way ensure to never store or even send credit card information to your server. The PAYONE Commerce Platform never needs access to the credit card information. The client side is responsible for safely retrieving a credit card token. This token must be used with this SDK.

### Apple Pay

When a client is successfully made a payment via ApplePay it receives a [ApplePayPayment](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypayment). This structure is accessible as the `ApplePayPayment` class. You can use the `ApplePayTransformer` to map an `ApplePayPayment` to a `MobilePaymentMethodSpecificInput` which can be used for payment executions or order requests. The transformer has a static method `transformApplePayPaymentToMobilePaymentMethodSpecificInput()` which takes an `ApplePayPayment` and returns a `MobilePaymentMethodSpecificInput`. The transformer does not check if the response is complete, if anything is missing the field will be set to `null`.

```python
from pcp_serversdk_python.models import ApplePayPayment, MobilePaymentMethodSpecificInput
from pcp_serversdk_python.transformer.ApplepayTransformer import transform_apple_pay_payment_to_mobile_payment_method_specific_input
import json

class App:
    def get_json_string_from_request_somehow(self):
        # Communicate with the client...
        message = ""
        return message

    def prepare_payment_for_apple_pay_payment(self):
        payment_json = self.get_json_string_from_request_somehow()
        payment = ApplePayPayment(**json.loads(payment_json))
        input = transform_apple_pay_payment_to_mobile_payment_method_specific_input(payment)
        # Wrap the input into a larger request and send to the PCP API
        # ...
    ...
```

**[back to top](#table-of-contents)**

## Demo App

```sh
API_KEY=api_key API_SECRET=api_secret MERCHANT_ID=123 COMMERCE_CASE_ID=234 CHECKOUT_ID=345 ./scripts.sh run
```

**[back to top](#table-of-contents)**

## Contributing

See [Contributing](./CONTRIBUTING.md)

**[back to top](#table-of-contents)**

## Releasing the library

### Preparing the Release

- Checkout develop branch
- Create release branch (release/0.1.0)

```sh
git checkout -b release/0.1.0
```

- Run `scripts.sh` script to set correct version

```sh
./scripts.sh version 0.1.0
```

### Changelog Generation with Conventional Changelog

When calling the `./scripts.sh version` script, the changelog will now be generated automatically using [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog).

1. **Conventional Commit Messages**:

   - Ensure all commit messages follow the conventional commit format, which is crucial for automatic changelog generation.
   - Commit messages should be in the format: `type(scope): subject`.

2. **Enforcing Commit Messages**:

   - We enforce conventional commit messages using [Lefthook](https://github.com/evilmartians/lefthook) with [commitlint](https://github.com/conventional-changelog/commitlint).
   - This setup ensures that all commit messages are validated before they are committed.

3. **Automatic Changelog Generation**:

   - The `./scripts.sh version` script will automatically generate and update the `CHANGELOG.md` file.
   - After running the script, review the updated changelog to ensure accuracy before proceeding with the release.

### Merging the Release Branch

- Create PR on `develop` branch
- Merge `develop` in `main` branch

### GitHub Action for Release

After successfully merging all changes to the `main` branch, an admin can trigger a GitHub Action to finalize and publish the release. This action ensures that the release process is automated, consistent, and deploys the new release from the `main` branch.

**Triggering the GitHub Action**:

- Only admins can trigger the release action.
- Ensure that all changes are committed to the `main` branch.
- Navigate to the Actions tab on your GitHub repository and manually trigger the release action for the `main` branch.

### Optional: Creating a GitHub Release

Once the release has been published to PyPi, developers can start using the latest version of the SDK. However, if you want to make the release more visible and include detailed release notes, you can optionally create a GitHub release.

1. **Navigate to the Releases Page**: Go to the "Releases" section of your repository on GitHub.
2. **Draft a New Release**: Click "Draft a new release".
3. **Tag the Release**: Select the version tag that corresponds to the version you just published on npm (e.g., `v0.1.0`).
4. **Release Title**: Add a descriptive title for the release (e.g., `v0.1.0 - Initial Release`).
5. **Auto-Generated Release Notes**: GitHub can automatically generate release notes based on merged pull requests and commit history. You can review these notes, adjust the content, and highlight important changes.
6. **Publish the Release**: Once you're satisfied with the release notes, click "Publish release".

Creating a GitHub release is optional, but it can provide additional context and visibility for your users. For detailed guidance, refer to the [GitHub documentation on managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

**[back to top](#table-of-contents)**

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

Thank you for using our SDK for Online Payments! If you have any questions or need further assistance, feel free to open an issue or contact us.
