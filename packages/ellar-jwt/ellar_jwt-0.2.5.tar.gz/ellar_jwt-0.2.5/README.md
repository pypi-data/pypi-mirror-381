<p align="center">
  <a href="#" target="blank"><img src="https://python-ellar.github.io/ellar/img/EllarLogoB.png" width="200" alt="Ellar Logo" /></a>
</p>

![Test](https://github.com/eadwinCode/ellar-jwt/actions/workflows/test_full.yml/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/python-ellar/ellar-jwt)
[![PyPI version](https://badge.fury.io/py/ellar-jwt.svg)](https://badge.fury.io/py/ellar-jwt)
[![PyPI version](https://img.shields.io/pypi/v/ellar-jwt.svg)](https://pypi.python.org/pypi/ellar-jwt)
[![PyPI version](https://img.shields.io/pypi/pyversions/ellar-jwt.svg)](https://pypi.python.org/pypi/ellar-jwt)


## Introduction
JWT utilities module for Ellar.


## Installation
```shell
$(venv) pip install ellar-jwt
```

## Usage

Import `JWTModule`:

```python
from ellar.common import Module
from ellar_jwt import JWTModule


@Module(
    modules=[JWTModule.setup(signing_secret_key='my_private_key')]
)
class AuthModule:
    pass

```

Inject `JWTService` where its needed as shown below

```python
from ellar_jwt import JWTService
from ellar.di import injectable


@injectable()
class AuthService:
  def __init__(self, jwt_service: JWTService) -> None:
    self.jwt_service = jwt_service

  async def sign_in(self, username: str, password: str) -> t.Dict:
      user = await self.user_service.find_one(username)
      if user.password != credentials.password:
          raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

      return {
          'access_token': await self.jwt_service.sign_async(user.dict())
      }
```

## JWTModule Setup
There are two ways in config JWTModule
- **setup**: 

  `JWTModule.setup` takes some parameters that allows instant configuration of the `JWTConfiguration` schema required by the `JWTService`
    
    For example:
    ```python
    from ellar.common import Module
    from ellar_jwt import JWTModule
    
    
    @Module(
        modules=[JWTModule.setup(signing_secret_key='my_private_key', issuer='https://google.com')]
    )
    class AuthModule:
        pass
    ```
- **register**:

    `JWTModule.register` lets you provide JWT configuration in the Ellar application config object using the `JWT_CONFIG` key. 
    The register function will create a `ModuleSetup` object that will inject application `config` to a JWT config factory
    
    for example:
    ```python
    # config.py
    import json
    from datetime import timedelta
    
    class DevelopmentConfig:
        JWT_CONFIG = {
            'algorithm':"HS256", # allow_algorithms=["HS256","HS384","HS512","RS256","RS384","RS512","ES256","ES384","ES512"]
            'leeway': 0, # t.Union[float, int, timedelta]
        
            'signing_secret_key': 'secret', # secret or private key
            'verifying_secret_key': "", # public key
            'audience': None,
        
            'issuer': None,
            'jwk_url': None,
        
            'jti': "jti",
            'lifetime': timedelta(minutes=5), # token lifetime, this will example in 5 mins
        
            'json_encoder':json.JSONEncoder # token lifetime, this will be an example 
        }
    ```
    In `auth/module.py`
    ```python
    from ellar.common import Module
    from ellar_jwt import JWTModule
        
        
    @Module(
        modules=[JWTModule.register_setup()]
    )
    class AuthModule:
        pass
    ```


## JWT Configuration Options
```python
import json
from datetime import timedelta


JWT_CONFIG = {
    'algorithm':"HS256", # allow_algorithms=["HS256","HS384","HS512","RS256","RS384","RS512","ES256","ES384","ES512"]
    'leeway': 0, # t.Union[float, int, timedelta]

    'signing_secret_key': 'secret', # secret or private key
    'verifying_secret_key': "", # public key
    'audience': None,

    'issuer': None,
    'jwk_url': None,

    'jti': "jti",
    'lifetime': timedelta(minutes=5), # token lifetime, this will example in 5 mins

    'json_encoder':json.JSONEncoder # token lifetime, this will be an example 
}
```

- ### `lifetime`
A `datetime.timedelta` object is employed to define the validity duration of the tokens. 
When generating a token, this `timedelta` value is combined with the present `UTC` time to establish the default `exp` claim value for the token.

- ### `algorithm`
The chosen algorithm from the `PyJWT` library governs the signing and verification procedures for tokens. 
For symmetric HMAC signing and verification, you have the option to use the following algorithms: `HS256`, `HS384`, and `HS512`. 
In the case of an HMAC algorithm, the signing_secret_key serves both as the signing and verifying key, rendering the `verifying_secret_key` setting redundant.
On the other hand, for asymmetric RSA signing and verification, you can opt for the following algorithms: `RS256`, `RS384`, and `RS512`. 
In this scenario, selecting an RSA algorithm mandates configuring the `signing_secret_key` setting with an RSA private key string. Correspondingly, the `verifying_secret_key` setting must contain an RSA public key string

- ### `signing_secret_key`
The signing key utilized for signing the content of generated tokens has distinct requirements based on the signing protocol. 
For HMAC signing, it should be a randomly generated string containing at least as many bits as dictated by the signing protocol. 
Conversely, an RSA signing should be a string encompassing an RSA private key with a length of 2048 bits or more.
As Simple JWT defaults to 256-bit HMAC signing, the `signing_secret_key` setting automatically takes on the value of your Django project's `SECRET_KEY`. 
While this default is practical, developers should modify this setting to a value separate from the Django project's secret key. 
This adjustment facilitates easier token signing key changes if the key is ever compromised.

- ### `verifying_secret_key`
The verification key is employed to authenticate the contents of generated tokens. 
In case an HMAC algorithm is indicated by the `algorithm` setting, the `verifying_secret_key` configuration is disregarded, and the `signing_secret_key` setting value will be utilized. 
However, if an RSA algorithm is designated by the `algorithm` setting, the `verifying_secret_key` parameter must be populated with an RSA public key string

- ### `audience`
The audience claim is incorporated into generated tokens and/or verified within decoded tokens. 
If configured as `None`, this element is omitted from tokens and isn't subjected to validation.

- ### `issuer`
The issuer claim is added to generated tokens and/or validated within decoded tokens. 
If configured as `None`, this attribute is omitted from tokens and isn't subjected to validation.

- ### `jwk_url`
The JWK_URL serves the purpose of dynamically retrieving the required public keys for token signature verification. 
For instance, with Auth0, you could configure it as 'https://yourdomain.auth0.com/.well-known/jwks.json'. 
If set to `None`, this field is omitted from the token backend and remains inactive during validation.

- ### `leeway`
Leeway provides a buffer for the expiration time, which can be defined as an integer representing seconds or a datetime.timedelta object. 
For further details, please consult the following link: https://pyjwt.readthedocs.io/en/latest/usage.html#expiration-time-claim-exp

- ### `jti`
The claim is designated for storing a token's unique identifier, which is utilized to distinguish revoked tokens within the blacklist application. 
There might be instances where an alternative claim other than the default "jti" claim needs to be employed for storing this value

- ### `json_encoder`
JSON Encoder class that will be used by the `PYJWT` to encode the `jwt_payload`.  



## API Spec

The `JwtService` uses [PYJWT](https://pypi.org/project/PyJWT/) underneath.

### _jwt_service.sign(payload: dict, headers: Dict[str, t.Any] = None, **jwt_config: t.Any) -> str_
Creates a jwt token for the provided payload. Also, you can override the default jwt config by using passing some keyword argument as a `jwt_config`

### _jwt_service.sign_async(payload: dict, headers: Dict[str, t.Any] = None, **jwt_config: t.Any) -> str_
Async action for `jwt_service.sign`

### _jwt_service.decode(token: str, verify: bool = True, **jwt_config: t.Any) -> t.Dict[str, t.Any]:_
Verifies and decodes provided token. And raises a JWTException exception if the token is invalid or expired

### _jwt_service.decode_async(token: str, verify: bool = True, **jwt_config: t.Any) -> t.Dict[str, t.Any]:_
Async action for `jwt_service.decode`


## License

Ellar is [MIT licensed](LICENSE).
