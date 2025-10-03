# Label Studio SSO - Generic JWT Integration

JWT 토큰을 사용한 범용 Label Studio SSO 플러그인

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 🎯 개요

이 패키지는 **모든 외부 시스템의 JWT 토큰**을 사용하여 Label Studio에 자동 로그인하는 범용 SSO 플러그인입니다.

> **원래 용도**: Things-Factory와 Label Studio 통합을 위해 개발되었으나, 이제 **어떤 JWT 기반 시스템과도 통합 가능**합니다.

### 특징

- ✅ **범용 JWT 지원**: 모든 JWT 기반 시스템과 통합 가능
- ✅ **간단한 설치**: `pip install label-studio-sso`
- ✅ **유연한 설정**: JWT claim 매핑 완전 커스터마이징
- ✅ **비침투적**: Label Studio 원본 코드 수정 없음
- ✅ **완전 독립**: Label Studio 버전 업그레이드 영향 없음
- ✅ **자동 사용자 생성**: 옵션으로 사용자 자동 생성 지원

---

## 📦 설치

### 1. pip으로 설치

```bash
pip install label-studio-sso
```

### 2. 환경 변수 설정

```bash
# 필수: JWT 시크릿 키 (외부 시스템과 공유)
export JWT_SSO_SECRET="your-shared-secret-key"

# 선택: 추가 설정 (기본값이 있음)
export JWT_SSO_ALGORITHM="HS256"              # JWT 알고리즘 (기본: HS256)
export JWT_SSO_TOKEN_PARAM="token"            # URL 파라미터 이름 (기본: token)
export JWT_SSO_EMAIL_CLAIM="email"            # 이메일 claim 이름 (기본: email)
export JWT_SSO_AUTO_CREATE_USERS="false"      # 사용자 자동 생성 (기본: false)
```

### 3. Label Studio settings.py 수정

```python
# label_studio/core/settings/base.py

INSTALLED_APPS = [
    # ... 기존 앱들 ...
    'label_studio_sso',  # ✅ 추가
]

AUTHENTICATION_BACKENDS = [
    'label_studio_sso.backends.JWTAuthenticationBackend',  # ✅ 추가 (최우선)
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'core.middleware.DisableCSRF',
    'django.middleware.csrf.CsrfViewMiddleware',
    'core.middleware.XApiKeySupportMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'label_studio_sso.middleware.JWTAutoLoginMiddleware',  # ✅ 추가
    # ... 나머지 미들웨어 ...
]

# JWT SSO 설정
JWT_SSO_SECRET = os.getenv('JWT_SSO_SECRET')
JWT_SSO_ALGORITHM = os.getenv('JWT_SSO_ALGORITHM', 'HS256')
JWT_SSO_TOKEN_PARAM = os.getenv('JWT_SSO_TOKEN_PARAM', 'token')
JWT_SSO_EMAIL_CLAIM = os.getenv('JWT_SSO_EMAIL_CLAIM', 'email')
JWT_SSO_USERNAME_CLAIM = os.getenv('JWT_SSO_USERNAME_CLAIM', None)  # None이면 email 사용
JWT_SSO_FIRST_NAME_CLAIM = os.getenv('JWT_SSO_FIRST_NAME_CLAIM', 'first_name')
JWT_SSO_LAST_NAME_CLAIM = os.getenv('JWT_SSO_LAST_NAME_CLAIM', 'last_name')
JWT_SSO_AUTO_CREATE_USERS = os.getenv('JWT_SSO_AUTO_CREATE_USERS', 'false').lower() == 'true'
```

### 4. Things-Factory와 통합하는 경우

Things-Factory 전용 backward compatibility alias를 사용할 수 있습니다:

```python
# 기존 Things-Factory 설정도 그대로 작동
AUTHENTICATION_BACKENDS = [
    'label_studio_sso.backends.ThingsFactoryJWTBackend',  # 여전히 작동
    # ...
]

MIDDLEWARE = [
    # ...
    'label_studio_sso.middleware.ThingsFactoryAutoLoginMiddleware',  # 여전히 작동
    # ...
]

# Things-Factory용 간단한 설정
THINGS_FACTORY_JWT_SECRET = os.getenv('THINGS_FACTORY_JWT_SECRET')
# 내부적으로 JWT_SSO_SECRET으로 자동 매핑됨
```

---

## 🚀 사용 방법

### 사용 사례

#### 사례 1: Things-Factory 통합

Things-Factory에서 Label Studio를 iframe으로 임베드하고 자동 로그인:

```javascript
// Things-Factory에서 JWT 토큰 생성
const token = jwt.sign(
  { email: 'user@example.com', name: 'John Doe' },
  process.env.JWT_SECRET,
  { expiresIn: '10m' }
)

// Label Studio URL with token
const labelStudioUrl = `https://label-studio.example.com?token=${token}`
```

#### 사례 2: 커스텀 포털 통합

자체 제작한 웹 포털에서 Label Studio로 SSO 연결:

```python
# 커스텀 포털에서 JWT 토큰 생성
import jwt
from datetime import datetime, timedelta

token = jwt.encode({
    'email': user.email,
    'first_name': user.first_name,
    'last_name': user.last_name,
    'exp': datetime.utcnow() + timedelta(minutes=10)
}, settings.JWT_SECRET, algorithm='HS256')

# Label Studio로 리다이렉트
redirect_url = f"https://label-studio.example.com?token={token}"
```

#### 사례 3: 기존 인증 시스템 통합

기존 JWT 기반 인증 시스템과 통합 (custom claim 매핑):

```bash
# JWT 토큰에 user_email 필드를 사용하는 경우
export JWT_SSO_EMAIL_CLAIM="user_email"
export JWT_SSO_USERNAME_CLAIM="username"
export JWT_SSO_FIRST_NAME_CLAIM="given_name"
export JWT_SSO_LAST_NAME_CLAIM="family_name"
```

### Things-Factory에서 설정

1. **Label Studio 설정 등록** (GraphQL)

```graphql
mutation {
  updateLabelStudioConfig(
    config: {
      serverUrl: "https://label-studio.example.com"
      apiToken: "YOUR_LABEL_STUDIO_API_TOKEN"
      ssoEnabled: true
      ssoTokenParam: "token"
      active: true
    }
  ) {
    id
  }
}
```

2. **사용자 동기화** (GraphQL)

```graphql
mutation {
  syncAllUsersToLabelStudio {
    total
    created
    updated
  }
}
```

3. **Label Studio 메뉴 접근**
   - Things-Factory에서 "Label Studio" 메뉴 클릭
   - 자동으로 Label Studio에 로그인됨 ✅

---

## 🔧 작동 원리

```
┌─────────────────────────────────────┐
│     Things-Factory                  │
│  1. JWT 토큰 발급                    │
│  2. iframe URL 생성                 │
│     https://ls.com?token=eyJhbGc... │
└────────────┬────────────────────────┘
             │
             │ iframe with JWT token
             ▼
┌─────────────────────────────────────┐
│     Label Studio                    │
│  3. Middleware: token 추출          │
│  4. JWT 검증 (공유 시크릿)           │
│  5. 이메일로 User 조회              │
│  6. 자동 로그인 ✅                   │
└─────────────────────────────────────┘
```

---

## 🔒 보안

### JWT 토큰 보안

- **HTTPS 필수**: 토큰이 URL에 포함되므로 HTTPS 사용 필수
- **짧은 유효기간**: 5-10분 권장
- **시크릿 관리**: 환경 변수로 관리, 절대 코드에 하드코딩 금지

### 시크릿 생성 (권장)

```python
import secrets
secret = secrets.token_urlsafe(32)
print(f"THINGS_FACTORY_JWT_SECRET={secret}")
```

---

## 🧪 테스트

### 로컬 테스트

```bash
# 1. 환경 변수 설정
export JWT_SSO_SECRET="test-secret-key"

# 2. Label Studio 실행
python label_studio/manage.py runserver

# 3. 테스트 토큰 생성
python -c "
import jwt
from datetime import datetime, timedelta
token = jwt.encode({
    'email': 'test@example.com',
    'first_name': 'John',
    'last_name': 'Doe',
    'iat': datetime.utcnow(),
    'exp': datetime.utcnow() + timedelta(minutes=10)
}, 'test-secret-key', algorithm='HS256')
print(f'http://localhost:8080?token={token}')
"

# 4. 브라우저에서 URL 열기
```

### 커스텀 JWT Claim 매핑 테스트

다른 JWT claim 구조를 사용하는 경우:

```bash
# 설정: user_email 필드 사용
export JWT_SSO_EMAIL_CLAIM="user_email"
export JWT_SSO_USERNAME_CLAIM="username"

# 토큰 생성
python -c "
import jwt
from datetime import datetime, timedelta
token = jwt.encode({
    'user_email': 'test@example.com',  # 커스텀 claim 이름
    'username': 'testuser',
    'iat': datetime.utcnow(),
    'exp': datetime.utcnow() + timedelta(minutes=10)
}, 'test-secret-key', algorithm='HS256')
print(f'http://localhost:8080?token={token}')
"
```

### 단위 테스트

```bash
cd /path/to/label-studio
python manage.py test label_studio_sso
```

---

## 📋 요구사항

- Python: 3.8+
- Label Studio: 1.7.0+
- PyJWT: 2.0+

---

## 🛠️ 개발

### 소스 설치

```bash
git clone https://github.com/your-org/label-studio-sso.git
cd label-studio-sso
pip install -e .
```

### 테스트 실행

```bash
pytest tests/
```

### 빌드

```bash
python -m build
```

---

## 📝 라이선스

MIT License

---

## 🤝 기여

이슈 및 풀 리퀘스트 환영합니다!

---

## 🔗 관련 프로젝트

- [Label Studio](https://github.com/HumanSignal/label-studio) - 오픈소스 데이터 라벨링 플랫폼
- [Things-Factory](https://github.com/hatiolab/things-factory) - 이 패키지의 원래 통합 대상
- [integration-label-studio](../things-factory/packages/integration-label-studio) - Things-Factory용 통합 모듈

## 🌟 적용 가능한 시스템

이 패키지는 다음과 같은 시스템과 통합할 수 있습니다:

- ✅ Things-Factory (원래 용도)
- ✅ 커스텀 Node.js/Express 어플리케이션
- ✅ Django/Flask 기반 웹 포털
- ✅ Spring Boot 기반 엔터프라이즈 시스템
- ✅ .NET Core 웹 어플리케이션
- ✅ 모든 JWT 발급 가능한 시스템

---

## 📞 문의

문제가 있으시면 [Issues](https://github.com/your-org/label-studio-sso/issues)에 등록해주세요.
