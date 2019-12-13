curl \
  -X GET \
  -G "https://login.linuxacademy.com/authorize" \
  -d "client_id=KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx" \
  -d "response_type=token"

# ./click-login.sh =>
# Found. Redirecting to /login?
#   state=g6Fo2SBIeGVwbWlYR1Jad1JMU0JZcG8yUFh2ZmhuQkZVUE1jbaN0aWTZIHVaTmF3d0lkMTBFOTJMbFM4NTR2UVpHM0RtUDQ3T0Njo2NpZNkgS2FXeE5uMUMyR2M3bjgzVzlPRmVYbHRkOFV0YjV2dng
#   &client=KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx
#   &protocol=oauth2
#   &response_type=token
#
# Add '-L' to follow redirect to login page


