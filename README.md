## Deployment Guide

---

### 1. Install AWS-CLI
Ref: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html

### 2. Configure AWS-CLI
```json
    $ aws configure
    AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
    AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    Default region name [None]: us-west-2
    Default output format [None]: json
```
Ref: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

### 3. Install serverless CLI
```json
    npm install -g serverless
```
Ref: https://www.serverless.com/framework/docs/getting-started/

### 4. install Python requirements 
```json
    pip install -r requirements.txt
```

### 5. Install serverless dependencies
```json
    npm install
```

### 6. Deploy serverless project
```json
    sls deploy -v
```

Ref: https://www.serverless.com/framework/docs/providers/aws/cli-reference/deploy/

---
Contact dev@pycoach.me for further support!
