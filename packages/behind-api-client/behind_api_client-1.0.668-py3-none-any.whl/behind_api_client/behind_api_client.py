import requests
from typing import Dict, Any, Callable, Optional
from .mailer.mailer_app import MailerApp
from .sales.sales_app import SalesApp
from .gpt.gpt_app import GptApp
from .globals.globals_app import GlobalsApp
from .monitor.monitor_app import MonitorApp
from .chat.chat_app import ChatApp
from .storage.storage_app import StorageApp
from .raet.raet_app import RaetApp
from .mastogram.mastogram_app import MastogramApp
from .tools.tools_app import ToolsApp
from .payments.payments_app import PaymentsApp
from .oauth.oauth_app import OauthApp
from .tests.tests_app import TestsApp
from .ru_kitchen.ru_kitchen_app import RuKitchenApp
from .sip.sip_app import SipApp
from .questionnaire.questionnaire_app import QuestionnaireApp
from .easyjob.easyjob_app import EasyjobApp
from .rag.rag_app import RagApp


class BehindApiClient:
    def __init__(self, endpoint: str, access_token: Optional[str] = None):
        self.endpoint = endpoint
        self.access_token = access_token
        self.selfsigned = False
        
        # Event handlers
        self.on_expired_handler: Callable = lambda data: None
        self.on_reject_handler: Callable = lambda data: None
        self.on_too_many_requests_handler: Callable = lambda data: None
        
        # Initialize app modules
        self.mailer = MailerApp(self)
        self.sales = SalesApp(self)
        self.gpt = GptApp(self)
        self.globals = GlobalsApp(self)
        self.monitor = MonitorApp(self)
        self.chat = ChatApp(self)
        self.storage = StorageApp(self)
        self.raet = RaetApp(self)
        self.mastogram = MastogramApp(self)
        self.tools = ToolsApp(self)
        self.payments = PaymentsApp(self)
        self.oauth = OauthApp(self)
        self.tests = TestsApp(self)
        self.ru_kitchen = RuKitchenApp(self)
        self.sip = SipApp(self)
        self.questionnaire = QuestionnaireApp(self)
        self.easyjob = EasyjobApp(self)
        self.rag = RagApp(self)

    def on_expired(self, callback: Callable):
        """Set callback for expired token events"""
        if callable(callback):
            self.on_expired_handler = callback

    def on_reject(self, callback: Callable):
        """Set callback for rejected request events"""
        if callable(callback):
            self.on_reject_handler = callback

    def on_too_many_requests(self, callback: Callable):
        """Set callback for rate limit events"""
        if callable(callback):
            self.on_too_many_requests_handler = callback

    def request(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Generic request method that parses endpoint string"""
        parts = endpoint.strip('/').split('/')
        
        app = parts[0] if len(parts) > 0 else None
        version = parts[1] if len(parts) > 1 else None
        module = parts[2] if len(parts) > 2 else None
        method = parts[3] if len(parts) > 3 else None
        
        return self.api_request(app, version, module, method, data or {})

    def api_request(self, app: str, version: str, module: str, action: str, 
                   data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make API request"""
        post_data = data.copy() if data else {}
        
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        
        if self.access_token:
            post_data['access_token'] = self.access_token
            headers['AccessToken'] = self.access_token
            headers['Authorization'] = f'Bearer {self.access_token}'
        
        try:
            url = f"{self.endpoint}/api/{app}/{version}/{module}/{action}"
            response = requests.post(url, json=post_data, headers=headers, verify=not self.selfsigned)
            
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get('success'):
                    return response_data
                else:
                    raise Exception(f"Request failed: {response_data}")
            else:
                try:
                    response_data = response.json()
                    code = response_data.get('code')
                    
                    if code in [1001, 1009]:
                        self.on_reject_handler(response_data)
                    if code == 1039:
                        self.on_too_many_requests_handler(response_data)
                    
                    raise Exception(response_data.get('message', 'Request failed'))
                except ValueError:
                    raise Exception(f"HTTP {response.status_code}: {response.text}")
        except requests.RequestException as e:
            raise Exception(f"Request error: {str(e)}")