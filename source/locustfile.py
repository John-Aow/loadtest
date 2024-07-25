from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 5)
    token = ""
    sid=""
    host = "https://trust-uat.ldblao.la"
    @task
    def on_start(self):
        self.token = self.get_token()

    def get_token(self):
        url = 'https://idp-app.ldblao.la/realms/uat-trust/protocol/openid-connect/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'password',
            'client_id': 'trust-customer-app-client',
            'client_secret': 'MvXmHhG7eMx2hAAA8KwYO3F3MYd9ON1g',
            'username': '2054666354',
            'password': '111111'
        }
        response = self.client.post(url, headers=headers, data=data)
        return response.json()["access_token"]

    @task
    def endpoint_with_token(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("https://trust-uat.ldblao.la/api/v4/customer/banking/statement/accounts/0300100010000034?pageNo=0", headers=headers)

    
    # @task
    # def getHomeConfig(self):
    #     headers = {"X-Lang": "en"}
    #     self.client.get("https://trust-uat.ldblao.la/api/v4/static/homeConfig", headers=headers)

    # @task
    # def getMobileCheck(self):
    #     self.client.get("https://trust-uat.ldblao.la/api/v4/user/checkMobileNo?q=2054666354")

    
    # @task
    # def call_get_account_info(self):
    #     headers = {
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     data = {
    #         'accountNo': '0300100010000014'
    #     }
    #     self.client.post('https://ldb-onprem1-mbinhouse-t24gtw-stmt-dev.ldblao.la/api/v4/t24info/getAccountInfo', headers=headers, data=data)

    # @task
    # def call_do_fund_transfer(self):
    #     headers = {
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     data = {
    #         'action': 'VALIDATE',
    #         'txnType': 'ACMB',
    #         'debitAcct': '0300100010000088',
    #         'debitCurrency': 'LAK',
    #         'debitAmount': '100',
    #         'creditAcct': '0300100010000068',
    #         'creditCurrency': 'LAK',
    #         'creditAmount': '',
    #         'customerName': '',
    #         'mobileNumber': '2077996693',
    #         'billNo': 'TEST202407170001',
    #         'detail': 'TEST LOAD TEST',
    #         'txnRef': 'TEST202407170001',
    #         'chargeType': 'PAYROLL',
    #         'chargeCurrency': 'LAK',
    #         'chargeAmount': '0'
    #     }
    #     self.client.post('https://ldb-onprem1-mbinhouse-t24gtw-ft-dev.ldblao.la/api/v4/t24finance/doFundTransfer', headers=headers, data=data)


    # @task
    # def getWaterBill(self):
    #     headers = {
    #         'X-Lang': 'eng',
    #         'X-Device-Id': '2E67307F-8A76-46A3-8130-E115152C68DB',
    #         'X-Device-System': 'iOS',
    #         'X-Device-Info': 'iPhone12,1',
    #         'X-Device-Is-Physical': 'true',
    #         'X-App-Version': '2.11.05',
    #         'X-Lat': '22.150602384562795',
    #         'X-Lng': '101.81658076872999',
    #         'X-Request-Id': 'dd7c05de21c5b963cc10781a53a77780',
    #         'Authorization': f'Bearer {self.token}',
    #         'Cookie': 'JSESSIONID=74349EA5197CAE3F08E01196B13D160B'
    #     }
    #     self.client.get("https://trust-uat.ldblao.la/api/v4/customer/billers/water/options", headers=headers)

    
    # @task
    # def getPaymentgetInfo(self):
    #     headers = {
    #         'X-Lang': 'eng',
    #         'X-Device-Id': '2E67307F-8A76-46A3-8130-E115152C68DB',
    #         'X-Device-System': 'iOS',
    #         'X-Device-Info': 'iPhone12,1',
    #         'X-Device-Is-Physical': 'true',
    #         'X-App-Version': '2.11.05',
    #         'X-Lat': '22.150602384562795',
    #         'X-Lng': '101.81658076872999',
    #         'X-Request-Id': 'dd7c05de21c5b963cc10781a53a77780',
    #         'Content-Type': 'application/json',
    #         'Authorization': f'Bearer {self.token}',
    #         'Cookie': 'JSESSIONID=74349EA5197CAE3F08E01196B13D160B'
    #     }
    #     data = {
    #         "biller": "water",
    #         "water": {
    #             "accountNo": "43603318",
    #             "branchId": 1
    #         }
    #     }
    #     self.client.post('https://trust-uat.ldblao.la/api/v4/customer/billers/water/getInfo', headers=headers, data=data)

    # @task
    # def getPaymentValidate(self):
    #     headers = {
    #         'X-Lang': 'eng',
    #         'X-Device-Id': '2E67307F-8A76-46A3-8130-E115152C68DB',
    #         'X-Device-System': 'iOS',
    #         'X-Device-Info': 'iPhone12,1',
    #         'X-Device-Is-Physical': 'true',
    #         'X-App-Version': '2.11.05',
    #         'X-Lat': '22.150602384562795',
    #         'X-Lng': '101.81658076872999',
    #         'X-Request-Id': 'dd7c05de21c5b963cc10781a53a77780',
    #         'Content-Type': 'application/json',
    #         'Authorization': f'Bearer {self.token}',
    #     }
    #     data = {
    #         "biller": "water",
    #         "water": {
    #             "mobileNo": "2054666354",
    #             "branchId": 2,
    #             "accountNo": "02010084",
    #             "paymentAmount": "1.00",
    #             "paymentDesc": "test",
    #             "debitAccountNo": "0300100010000088",
    #             "debitAccountCcy": "LAK",
    #             "debitAccountName": "JACQUES BOUNLIPHONE MR"
    # }
    #     }
    #     response = self.client.post('https://trust-uat.ldblao.la/api/v4/customer/billers/water/validate', headers=headers, data=data)
    #     if response.status_code == 200:
    #         response_data = response.json()
    #         self.sid = response_data['water']['sid']  # Save the SID from the validate response
    #         self.call_confirm_endpoint()

    # @task
    # def getPaymentConfirm(self):
    #     headers = {
    #         'X-Lang': 'eng',
    #         'X-Device-Id': '2E67307F-8A76-46A3-8130-E115152C68DB',
    #         'X-Device-System': 'iOS',
    #         'X-Device-Info': 'iPhone12,1',
    #         'X-Device-Is-Physical': 'true',
    #         'X-App-Version': '2.11.05',
    #         'X-Lat': '22.150602384562795',
    #         'X-Lng': '101.81658076872999',
    #         'X-Request-Id': 'dd7c05de21c5b963cc10781a53a77780',
    #         'Content-Type': 'application/json',
    #         'Authorization': f'Bearer {self.token}',
    #         'Cookie': 'JSESSIONID=74349EA5197CAE3F08E01196B13D160B'
    #     }
    #     data = {
    #         "biller": "water",
    #         "water": {
    #             "sid": self.sid,
    #             "mobileNo": "2054666354",
    #             "submittedAt": datetime.now().isoformat()
    #         }
    #     }
    #     self.client.post('https://trust-uat.ldblao.la/api/v4/customer/billers/water/confirm', headers=headers, data=data)