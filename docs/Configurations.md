# Configurations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_mode** | **str** | The auth mode of current system, such as \&quot;db_auth\&quot;, \&quot;ldap_auth\&quot;, \&quot;oidc_auth\&quot; | [optional] 
**email_from** | **str** | The sender name for Email notification. | [optional] 
**email_host** | **str** | The hostname of SMTP server that sends Email notification. | [optional] 
**email_identity** | **str** | By default it&#39;s empty so the email_username is picked | [optional] 
**email_insecure** | **bool** | Whether or not the certificate will be verified when Harbor tries to access the email server. | [optional] 
**email_password** | **str** | Email password | [optional] 
**email_port** | **int** | The port of SMTP server | [optional] 
**email_ssl** | **bool** | When it&#39;&#39;s set to true the system will access Email server via TLS by default.  If it&#39;&#39;s set to false, it still will handle \&quot;STARTTLS\&quot; from server side. | [optional] 
**email_username** | **str** | The username for authenticate against SMTP server | [optional] 
**ldap_base_dn** | **str** | The Base DN for LDAP binding. | [optional] 
**ldap_filter** | **str** | The filter for LDAP search | [optional] 
**ldap_group_base_dn** | **str** | The base DN to search LDAP group. | [optional] 
**ldap_group_admin_dn** | **str** | Specify the ldap group which have the same privilege with Harbor admin | [optional] 
**ldap_group_attribute_name** | **str** | The attribute which is used as identity of the LDAP group, default is cn.&#39; | [optional] 
**ldap_group_search_filter** | **str** | The filter to search the ldap group | [optional] 
**ldap_group_search_scope** | **int** | The scope to search ldap group. &#39;&#39;0-LDAP_SCOPE_BASE, 1-LDAP_SCOPE_ONELEVEL, 2-LDAP_SCOPE_SUBTREE&#39;&#39; | [optional] 
**ldap_scope** | **int** | The scope to search ldap users,&#39;0-LDAP_SCOPE_BASE, 1-LDAP_SCOPE_ONELEVEL, 2-LDAP_SCOPE_SUBTREE&#39; | [optional] 
**ldap_search_dn** | **str** | The DN of the user to do the search. | [optional] 
**ldap_search_password** | **str** | The password of the ldap search dn | [optional] 
**ldap_timeout** | **int** | Timeout in seconds for connection to LDAP server | [optional] 
**ldap_uid** | **str** | The attribute which is used as identity for the LDAP binding, such as \&quot;CN\&quot; or \&quot;SAMAccountname\&quot; | [optional] 
**ldap_url** | **str** | The URL of LDAP server | [optional] 
**ldap_verify_cert** | **bool** | Whether verify your OIDC server certificate, disable it if your OIDC server is hosted via self-hosted certificate. | [optional] 
**ldap_group_membership_attribute** | **str** | The user attribute to identify the group membership | [optional] 
**project_creation_restriction** | **str** | Indicate who can create projects, it could be &#39;&#39;adminonly&#39;&#39; or &#39;&#39;everyone&#39;&#39;. | [optional] 
**read_only** | **bool** | The flag to indicate whether Harbor is in readonly mode. | [optional] 
**self_registration** | **bool** | Whether the Harbor instance supports self-registration.  If it&#39;&#39;s set to false, admin need to add user to the instance. | [optional] 
**token_expiration** | **int** | The expiration time of the token for internal Registry, in minutes. | [optional] 
**uaa_client_id** | **str** | The client id of UAA | [optional] 
**uaa_client_secret** | **str** | The client secret of the UAA | [optional] 
**uaa_endpoint** | **str** | The endpoint of the UAA | [optional] 
**uaa_verify_cert** | **bool** | Verify the certificate in UAA server | [optional] 
**http_authproxy_endpoint** | **str** | The endpoint of the HTTP auth | [optional] 
**http_authproxy_tokenreview_endpoint** | **str** | The token review endpoint | [optional] 
**http_authproxy_admin_groups** | **str** | The group which has the harbor admin privileges | [optional] 
**http_authproxy_admin_usernames** | **str** | The username which has the harbor admin privileges | [optional] 
**http_authproxy_verify_cert** | **bool** | Verify the HTTP auth provider&#39;s certificate | [optional] 
**http_authproxy_skip_search** | **bool** | Search user before onboard | [optional] 
**http_authproxy_server_certificate** | **str** | The certificate of the HTTP auth provider | [optional] 
**oidc_name** | **str** | The OIDC provider name | [optional] 
**oidc_endpoint** | **str** | The endpoint of the OIDC provider | [optional] 
**oidc_client_id** | **str** | The client ID of the OIDC provider | [optional] 
**oidc_client_secret** | **str** | The OIDC provider secret | [optional] 
**oidc_groups_claim** | **str** | The attribute claims the group name | [optional] 
**oidc_admin_group** | **str** | The OIDC group which has the harbor admin privileges | [optional] 
**oidc_scope** | **str** | The scope of the OIDC provider | [optional] 
**oidc_user_claim** | **str** | The attribute claims the username | [optional] 
**oidc_verify_cert** | **bool** | Verify the OIDC provider&#39;s certificate&#39; | [optional] 
**oidc_auto_onboard** | **bool** | Auto onboard the OIDC user | [optional] 
**oidc_extra_redirect_parms** | **str** | Extra parameters to add when redirect request to OIDC provider | [optional] 
**robot_token_duration** | **int** | The robot account token duration in days | [optional] 
**robot_name_prefix** | **str** | The rebot account name prefix | [optional] 
**notification_enable** | **bool** | Enable notification | [optional] 
**quota_per_project_enable** | **bool** | Enable quota per project | [optional] 
**storage_per_project** | **int** | The storage quota per project | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

