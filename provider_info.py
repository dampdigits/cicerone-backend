PROVIDERS = {
    "google": {
        "domains": ["developers.google.com", "support.google.com", "cloud.google.com"],
        "seeds": ["https://developers.google.com/identity/protocols/oauth2"],
        "select_paths": [
            r"/identity/.*",
            r"/identity/protocols/oauth2.*",
            r"/identity/protocols/openid-connect.*",
            r"/workspace/guides/authorize.*",
            r"/drive/api/.*",
            r"/calendar/api/.*",
            r"/gmail/api/.*",
            r"/sheets/api/.*",
        ],
        "exclude_paths": [
            r".*/(samples?|codelabs?|blog|community|support|pricing|release-notes|whats-new).*",
        ],
    },
    "microsoft": {
        "domains": ["learn.microsoft.com", "developer.microsoft.com"],
        "seeds": ["https://learn.microsoft.com/en-us/entra/identity-platform/"],
        "select_paths": [
            r"/en-us/entra/identity-platform/.*",
            r"/en-us/entra/identity/enterprise-apps/.*",
            r"/en-us/graph/auth/.*",
            r"/en-us/graph/sdks/.*",
        ],
        "exclude_paths": [
            r".*/(samples?|whats-new|release-notes|msal-.*|training|community|pricing).*",
        ],
    },
    "apple": {
        "domains": ["developer.apple.com", "help.apple.com"],
        "seeds": ["https://developer.apple.com/documentation/signinwithapple"],
        "select_paths": [
            r"/documentation/signinwithapple.*",
            r"/documentation/authenticationservices.*",
            r"/documentation/security.*",
        ],
        "exclude_paths": [
            r".*/(videos|news|downloads|forums|sample-code|release-notes).*",
        ],
    },
    "amazon": {
        "domains": ["developer.amazon.com", "docs.aws.amazon.com"],
        "seeds": ["https://developer.amazon.com/docs/login-with-amazon/web-docs.html"],
        "select_paths": [
            r"/docs/login-with-amazon.*",
            r"/docs/.*/authentication.*",
            r"/docs/.*/authorization.*",
            r"/docs/.*/oauth.*",
        ],
        "exclude_paths": [
            r".*/(blog|news|careers|pricing|forums|samples?).*",
        ],
    },
    "meta": {
        "domains": ["developers.facebook.com", "developers.instagram.com"],
        "seeds": [
            "https://developers.facebook.com/documentation/facebook-login/guides/advanced/manual-flow"
        ],
        "select_paths": [
            r"/documentation/facebook-login/.*",
            r"/documentation/instagram-api/.*",
            r"/documentation/instagram-basic-display-api/.*",
            r"/documentation/permissions/.*",
        ],
        "exclude_paths": [
            r".*/(blog|news|careers|case-studies|success-stories|marketing).*",
        ],
    },
    "linkedin": {
        "domains": ["learn.microsoft.com", "developer.linkedin.com"],
        "seeds": [
            "https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow"
        ],
        "select_paths": [
            r"/en-us/linkedin/shared/authentication/.*",
            r"/en-us/linkedin/shared/api-guide/.*",
        ],
        "exclude_paths": [
            r".*/(blog|news|careers|pricing|community).*",
        ],
    },
    "github": {
        "domains": ["docs.github.com"],
        "seeds": ["https://docs.github.com/en/apps/oauth-apps"],
        "select_paths": [
            r"/en/apps/.*",
            r"/en/authentication/.*",
            r"/en/rest/.*",
            r"/en/graphql/.*",
            r"/en/webhooks/.*",
        ],
        "exclude_paths": [
            r".*/(guides|get-started|pricing|security|community|site-policy).*",
        ],
    },
    "gitlab": {
        "domains": ["docs.gitlab.com"],
        "seeds": ["https://docs.gitlab.com/api/oauth2/"],
        "select_paths": [
            r"/api/oauth2/.*",
            r"/api/rest/.*",
            r"/api/graphql/.*",
            r"/user/profile/account/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|install|release-notes|whats-new).*",
        ],
    },
    "atlassian": {
        "domains": ["developer.atlassian.com"],
        "seeds": [
            "https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/"
        ],
        "select_paths": [
            r"/cloud/confluence/oauth-2-3lo-apps/.*",
            r"/cloud/jira/platform/.*",
            r"/cloud/confluence/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|marketplace|pricing|changelog).*",
        ],
    },
    "salesforce": {
        "domains": ["developer.salesforce.com", "help.salesforce.com"],
        "seeds": [
            "https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart_oauth.htm"
        ],
        "select_paths": [
            r"/docs/atlas.en-us.api_rest.meta/api_rest/.*",
            r"/docs/atlas.en-us.identity.*/.*",
            r"/docs/atlas.en-us.*/.*oauth.*",
        ],
        "exclude_paths": [
            r".*/(trailhead|blog|release-notes|pricing|community).*",
        ],
    },
    "hubspot": {
        "domains": ["developers.hubspot.com", "knowledge.hubspot.com"],
        "seeds": [
            "https://developers.hubspot.com/docs/apps/legacy-apps/authentication/oauth-quickstart-guide"
        ],
        "select_paths": [
            r"/docs/apps/.*",
            r"/docs/api/.*",
            r"/docs/crm/.*",
        ],
        "exclude_paths": [
            r".*/(blog|academy|community|pricing|changelog).*",
        ],
    },
    "slack": {
        "domains": ["api.slack.com"],
        "seeds": ["https://docs.slack.dev/authentication/installing-with-oauth/"],
        "select_paths": [
            r"/authentication/.*",
            r"/reference/.*",
            r"/api/.*",
            r"/concepts/.*",
        ],
        "exclude_paths": [
            r".*/(blog|changelog|community|pricing|apps).*",
        ],
    },
    "zoom": {
        "domains": ["developers.zoom.us"],
        "seeds": ["https://developers.zoom.us/docs/integrations/oauth/"],
        "select_paths": [
            r"/docs/integrations/oauth/.*",
            r"/docs/integrations/.*",
            r"/docs/api-reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|events|community|release-notes).*",
        ],
    },
    "dropbox": {
        "domains": ["developers.dropbox.com"],
        "seeds": ["https://docs.dropboxapi.com/dropbox-api/docs/oauth"],
        "select_paths": [
            r"/dropbox-api/docs/oauth.*",
            r"/dropbox-api/docs/.*",
            r"/dropbox-api/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|help).*",
        ],
    },
    "box": {
        "domains": ["developer.box.com"],
        "seeds": ["https://developer.box.com/guides/authentication/oauth/"],
        "select_paths": [
            r"/guides/authentication/.*",
            r"/guides/.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|changelog).*",
        ],
    },
    "adobe": {
        "domains": ["developer.adobe.com", "helpx.adobe.com"],
        "seeds": [
            "https://developer.adobe.com/developer-console/docs/guides/authentication/"
        ],
        "select_paths": [
            r"/developer-console/docs/guides/authentication/.*",
            r"/developer-console/docs/.*",
            r"/apis/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|events|pricing|release-notes).*",
        ],
    },
    "shopify": {
        "domains": ["shopify.dev", "help.shopify.com"],
        "seeds": [
            "https://shopify.dev/docs/apps/build/authentication-authorization/authenticate-standalone-apps?lang=node"
        ],
        "select_paths": [
            r"/docs/apps/build/authentication-authorization/.*",
            r"/docs/apps/.*",
            r"/docs/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|changelog|community|pricing|release-notes).*",
        ],
    },
    "stripe": {
        "domains": ["docs.stripe.com", "dashboard.stripe.com"],
        "seeds": ["https://docs.stripe.com/connect/oauth-reference"],
        "select_paths": [
            r"/connect/oauth-reference.*",
            r"/connect/.*",
            r"/api/.*",
            r"/webhooks/.*",
        ],
        "exclude_paths": [
            r".*/(blog|changelog|pricing|gallery|support).*",
        ],
    },
    "paypal": {
        "domains": ["developer.paypal.com"],
        "seeds": ["https://developer.paypal.com/api/rest/authentication/"],
        "select_paths": [
            r"/api/rest/authentication/.*",
            r"/api/rest/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|newsroom|pricing|community).*",
        ],
    },
    "zoho": {
        "domains": ["help.zoho.com", "www.zoho.com"],
        "seeds": [
            "https://help.zoho.com/portal/en/kb/articles/oauth-2-0-for-zoho-apis"
        ],
        "select_paths": [
            r"/portal/en/kb/articles/oauth-2-0-for-zoho-apis.*",
            r"/books/api/.*",
            r"/crm/developer/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community|release-notes).*",
        ],
    },
    "notion": {
        "domains": ["developers.notion.com"],
        "seeds": [
            "https://developers.notion.com/guides/connections-and-tokens/overview"
        ],
        "select_paths": [
            r"/guides/connections-and-tokens/.*",
            r"/reference/.*",
            r"/guides/.*",
        ],
        "exclude_paths": [
            r".*/(blog|changelog|community|pricing).*",
        ],
    },
    "airtable": {
        "domains": ["airtable.com", "support.airtable.com"],
        "seeds": ["https://airtable.com/developers/web/api/oauth"],
        "select_paths": [
            r"/developers/web/api/oauth.*",
            r"/developers/web/api/.*",
            r"/developers/web/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|support|community).*",
        ],
    },
    "asana": {
        "domains": ["developers.asana.com"],
        "seeds": ["https://developers.asana.com/docs/oauth"],
        "select_paths": [
            r"/docs/oauth.*",
            r"/docs/.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|forum|pricing|release-notes).*",
        ],
    },
    "monday_com": {
        "domains": ["developer.monday.com"],
        "seeds": ["https://developer.monday.com/apps/docs/oauth/"],
        "select_paths": [
            r"/apps/docs/oauth/.*",
            r"/apps/docs/.*",
            r"/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|changelog).*",
        ],
    },
    "clickup": {
        "domains": ["developer.clickup.com", "help.clickup.com"],
        "seeds": ["https://developer.clickup.com/reference/oauth"],
        "select_paths": [
            r"/reference/oauth.*",
            r"/reference/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|release-notes).*",
        ],
    },
    "smartsheet": {
        "domains": ["developers.smartsheet.com"],
        "seeds": ["https://developers.smartsheet.com/api/basics#oauth-tokens"],
        "select_paths": [
            r"/api/basics#oauth-tokens.*",
            r"/api/.*",
            r"/sdks/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|release-notes).*",
        ],
    },
    "wrike": {
        "domains": ["developers.wrike.com"],
        "seeds": ["https://developers.wrike.com/oauth/"],
        "select_paths": [
            r"/oauth/.*",
            r"/api/.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing).*",
        ],
    },
    "basecamp": {
        "domains": ["github.com", "basecamp.com"],
        "seeds": [
            "https://github.com/basecamp/api/blob/master/sections/authentication.md"
        ],
        "select_paths": [
            r"/basecamp/api/blob/master/sections/authentication\.md.*",
            r"/basecamp/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|jobs|community).*",
        ],
    },
    "todoist": {
        "domains": ["developer.todoist.com"],
        "seeds": ["https://developer.todoist.com/api/v1/#tag/OAuth"],
        "select_paths": [
            r"/api/v1/#tag/OAuth.*",
            r"/api/v1/.*",
            r"/guides/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "teamwork": {
        "domains": ["developer.teamwork.com"],
        "seeds": ["https://developer.teamwork.com/guides/oauth/"],
        "select_paths": [
            r"/guides/oauth/.*",
            r"/guides/.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing).*",
        ],
    },
    "teamleader": {
        "domains": ["developers.teamleader.eu"],
        "seeds": ["https://developers.teamleader.eu/docs/authentication"],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "podio": {
        "domains": ["developers.podio.com"],
        "seeds": ["https://developers.podio.com/authentication"],
        "select_paths": [
            r"/authentication.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "miro": {
        "domains": ["developers.miro.com"],
        "seeds": ["https://developers.miro.com/docs/oauth"],
        "select_paths": [
            r"/docs/oauth.*",
            r"/docs/.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|release-notes).*",
        ],
    },
    "mural": {
        "domains": ["developers.mural.co"],
        "seeds": [
            "https://developers.mural.co/public/reference/authentication"
        ],
        "select_paths": [
            r"/public/reference/authentication.*",
            r"/public/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing).*",
        ],
    },
    "coda": {
        "domains": ["coda.io", "help.coda.io"],
        "seeds": ["https://coda.io/developers/apis/v1#section/OAuth2"],
        "select_paths": [
            r"/developers/apis/v1#section/OAuth2.*",
            r"/developers/apis/v1.*",
            r"/developers/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|changelog).*",
        ],
    },
    "quip": {
        "domains": ["developer.salesforce.com", "quip.com"],
        "seeds": [
            "https://developer.salesforce.com/docs/atlas.en-us.quip_dev.meta/quip_dev/quip_oauth.htm"
        ],
        "select_paths": [
            r"/docs/atlas.en-us.quip_dev.meta/quip_dev/.*",
            r"/docs/atlas.en-us.quip_dev.meta/.*",
        ],
        "exclude_paths": [
            r".*/(blog|trailhead|release-notes|pricing).*",
        ],
    },
    "evernote": {
        "domains": ["dev.evernote.com"],
        "seeds": ["https://dev.evernote.com/legacy/doc/articles/authentication"],
        "select_paths": [
            r"/legacy/doc/articles/authentication.*",
            r"/legacy/doc/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing).*",
        ],
    },
    "meistertask": {
        "domains": ["developers.meister.co"],
        "seeds": ["https://developers.meister.co/oauth"],
        "select_paths": [
            r"/oauth.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "proofhub": {
        "domains": ["developers.proofhub.com"],
        "seeds": ["https://developers.proofhub.com/docs/authentication"],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "nifty": {
        "domains": ["niftypm.com"],
        "seeds": ["https://niftypm.com/api"],
        "select_paths": [
            r"/api.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "docusign": {
        "domains": ["developers.docusign.com"],
        "seeds": ["https://developers.docusign.com/platform/auth/"],
        "select_paths": [
            r"/platform/auth/.*",
            r"/platform/.*",
            r"/esign/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|release-notes).*",
        ],
    },
    "pandadoc": {
        "domains": ["developers.pandadoc.com"],
        "seeds": ["https://developers.pandadoc.com/reference/auth-overview"],
        "select_paths": [
            r"/reference/auth-overview.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "signnow": {
        "domains": ["docs.signnow.com", "api-eu.signnow.com"],
        "seeds": ["https://docs.signnow.com/docs/authentication"],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "dropbox_sign": {
        "domains": ["app.hellosign.com", "developers.hellosign.com"],
        "seeds": ["https://developers.hellosign.com/api/oauth/"],
        "select_paths": [
            r"/api/oauth/.*",
            r"/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "boldsign": {
        "domains": ["boldsign.com"],
        "seeds": [
            "https://boldsign.com/api/api-documentation/version/v1/tag/Authentication/"
        ],
        "select_paths": [
            r"/api/api-documentation/version/v1/tag/Authentication/.*",
            r"/api/api-documentation/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "formstack": {
        "domains": ["developers.formstack.com"],
        "seeds": ["https://developers.formstack.com/docs/oauth-2-0"],
        "select_paths": [
            r"/docs/oauth-2-0.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "typeform": {
        "domains": ["developers.typeform.com"],
        "seeds": [
            "https://developers.typeform.com/get-started/personal-access-tokens/"
        ],
        "select_paths": [
            r"/get-started/personal-access-tokens/.*",
            r"/get-started/.*",
            r"/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "jotform": {
        "domains": ["api.jotform.com"],
        "seeds": ["https://api.jotform.com/docs/"],
        "select_paths": [
            r"/docs/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "surveymonkey": {
        "domains": ["developer.surveymonkey.com"],
        "seeds": ["https://developer.surveymonkey.com/api/v3/#oauth"],
        "select_paths": [
            r"/api/v3/#oauth.*",
            r"/api/v3/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "surveysparrow": {
        "domains": ["developers.surveysparrow.com"],
        "seeds": [
            "https://developers.surveysparrow.com/rest-api/authentication"
        ],
        "select_paths": [
            r"/rest-api/authentication.*",
            r"/rest-api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "calendly": {
        "domains": ["developer.calendly.com"],
        "seeds": ["https://developer.calendly.com/docs/oauth-overview"],
        "select_paths": [
            r"/docs/oauth-overview.*",
            r"/docs/.*",
            r"/api-reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "acuity_scheduling": {
        "domains": ["developers.acuityscheduling.com"],
        "seeds": ["https://developers.acuityscheduling.com/docs/oauth"],
        "select_paths": [
            r"/docs/oauth.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "cronofy": {
        "domains": ["developer.cronofy.com"],
        "seeds": ["https://developer.cronofy.com/authentication.html"],
        "select_paths": [
            r"/authentication\.html.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "cal_com": {
        "domains": ["cal.com", "developer.cal.com"],
        "seeds": ["https://cal.com/docs/api-reference/authentication"],
        "select_paths": [
            r"/docs/api-reference/authentication.*",
            r"/docs/api-reference/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "youcanbookme": {
        "domains": ["developers.youcanbook.me"],
        "seeds": ["https://developers.youcanbook.me/docs/oauth"],
        "select_paths": [
            r"/docs/oauth.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "oncehub": {
        "domains": ["developers.oncehub.com"],
        "seeds": ["https://developers.oncehub.com/docs/oauth"],
        "select_paths": [
            r"/docs/oauth.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "simplybook_me": {
        "domains": ["simplybook.me", "developer.simplybook.me"],
        "seeds": ["https://developer.simplybook.me/index.php/Using_the_API"],
        "select_paths": [
            r"/index.php/Using_the_API.*",
            r"/index.php/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "zoho_bookings": {
        "domains": ["help.zoho.com", "www.zoho.com"],
        "seeds": ["https://www.zoho.com/bookings/help/api/oauth.html"],
        "select_paths": [
            r"/bookings/help/api/oauth\.html.*",
            r"/bookings/help/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "google_workspace": {
        "domains": ["developers.google.com", "developers.googleworkspace.com"],
        "seeds": ["https://developers.google.com/workspace/guides/authorize"],
        "select_paths": [
            r"/workspace/guides/authorize.*",
            r"/workspace/guides/.*",
            r"/workspace/.*",
        ],
        "exclude_paths": [
            r".*/(samples?|codelabs?|blog|community|pricing).*",
        ],
    },
    "microsoft_365": {
        "domains": ["learn.microsoft.com", "developer.microsoft.com"],
        "seeds": ["https://learn.microsoft.com/en-us/graph/auth/"],
        "select_paths": [
            r"/en-us/graph/auth/.*",
            r"/en-us/graph/.*",
            r"/en-us/entra/identity-platform/.*",
        ],
        "exclude_paths": [
            r".*/(samples?|whats-new|release-notes|msal-.*|training).*",
        ],
    },
    "pipedrive": {
        "domains": ["developers.pipedrive.com"],
        "seeds": [
            "https://developers.pipedrive.com/docs/api/v1/#section/Authentication/OAuth-authorization"
        ],
        "select_paths": [
            r"/docs/api/v1/#section/Authentication/OAuth-authorization.*",
            r"/docs/api/v1/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "close": {
        "domains": ["developer.close.com"],
        "seeds": ["https://developer.close.com/#authentication"],
        "select_paths": [
            r"/#authentication.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "copper": {
        "domains": ["developer.copper.com"],
        "seeds": ["https://developer.copper.com/authentication.html"],
        "select_paths": [
            r"/authentication\.html.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "attio": {
        "domains": ["developers.attio.com"],
        "seeds": ["https://developers.attio.com/docs/authentication"],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "insightly": {
        "domains": ["api.na1.insightly.com", "developers.insightly.com"],
        "seeds": [
            "https://api.na1.insightly.com/v3.1/Docs#!/Overview/Authentication"
        ],
        "select_paths": [
            r"/v3\.1/Docs#!/Overview/Authentication.*",
            r"/v3\.1/Docs.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "keap": {
        "domains": ["developer.infusionsoft.com"],
        "seeds": [
            "https://developer.infusionsoft.com/docs/rest/#section/Authentication"
        ],
        "select_paths": [
            r"/docs/rest/#section/Authentication.*",
            r"/docs/rest/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "zendesk": {
        "domains": ["developer.zendesk.com", "support.zendesk.com"],
        "seeds": [
            "https://developer.zendesk.com/api-reference/ticketing/introduction/#authentication"
        ],
        "select_paths": [
            r"/api-reference/ticketing/introduction/#authentication.*",
            r"/api-reference/.*",
            r"/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|changelog).*",
        ],
    },
    "freshworks": {
        "domains": ["developers.freshworks.com"],
        "seeds": ["https://developers.freshworks.com/docs/api/"],
        "select_paths": [
            r"/docs/api/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|release-notes).*",
        ],
    },
    "intercom": {
        "domains": ["developers.intercom.com"],
        "seeds": [
            "https://developers.intercom.com/docs/build-an-oauth-app"
        ],
        "select_paths": [
            r"/docs/build-an-oauth-app.*",
            r"/docs/.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|changelog).*",
        ],
    },
    "help_scout": {
        "domains": ["developer.helpscout.com"],
        "seeds": [
            "https://developer.helpscout.com/mailbox-api/authorization/oauth2/"
        ],
        "select_paths": [
            r"/mailbox-api/authorization/oauth2/.*",
            r"/mailbox-api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "front": {
        "domains": ["dev.frontapp.com"],
        "seeds": ["https://dev.frontapp.com/docs/authentication"],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "gorgias": {
        "domains": ["developers.gorgias.com"],
        "seeds": [
            "https://developers.gorgias.com/reference/authentication"
        ],
        "select_paths": [
            r"/reference/authentication.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "kustomer": {
        "domains": ["developer.kustomer.com"],
        "seeds": [
            "https://developer.kustomer.com/authentication/docs/authentication"
        ],
        "select_paths": [
            r"/authentication/docs/authentication.*",
            r"/authentication/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "livechat": {
        "domains": ["developers.livechat.com"],
        "seeds": ["https://developers.livechat.com/docs/authorization/"],
        "select_paths": [
            r"/docs/authorization/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "tidio": {
        "domains": ["developers.tidio.com"],
        "seeds": ["https://developers.tidio.com/authentication"],
        "select_paths": [
            r"/authentication.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "reamaze": {
        "domains": ["developers.reamaze.com"],
        "seeds": ["https://developers.reamaze.com/#authentication"],
        "select_paths": [
            r"/#authentication.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "dixa": {
        "domains": ["docs.dixa.io"],
        "seeds": ["https://docs.dixa.io/#section/Authentication"],
        "select_paths": [
            r"/#section/Authentication.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "superoffice": {
        "domains": ["docs.superoffice.com"],
        "seeds": [
            "https://docs.superoffice.com/en/api/authentication/online/index.html"
        ],
        "select_paths": [
            r"/en/api/authentication/online/index\.html.*",
            r"/en/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "blackbaud": {
        "domains": ["developer.blackbaud.com"],
        "seeds": [
            "https://developer.blackbaud.com/skyapi/docs/authorization"
        ],
        "select_paths": [
            r"/skyapi/docs/authorization.*",
            r"/skyapi/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "servicetitan": {
        "domains": ["developer.servicetitan.com"],
        "seeds": ["https://developer.servicetitan.io/docs/api/authentication"],
        "select_paths": [
            r"/docs/api/authentication.*",
            r"/docs/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "mailchimp": {
        "domains": ["mailchimp.com", "developer.mailchimp.com"],
        "seeds": [
            "https://mailchimp.com/developer/marketing/build/start-developing/set-up-an-oauth-app"
        ],
        "select_paths": [
            r"/developer/marketing/build/start-developing/set-up-an-oauth-app.*",
            r"/developer/marketing/.*",
            r"/developer/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "constant_contact": {
        "domains": ["developer.constantcontact.com"],
        "seeds": [
            "https://developer.constantcontact.com/api_guide/oauth2_overview.html"
        ],
        "select_paths": [
            r"/api_guide/oauth2_overview\.html.*",
            r"/api_guide/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "aweber": {
        "domains": ["api.aweber.com"],
        "seeds": ["https://api.aweber.com/#tag/OAuth"],
        "select_paths": [
            r"/#tag/OAuth.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "activecampaign": {
        "domains": ["developers.activecampaign.com"],
        "seeds": [
            "https://developers.activecampaign.com/reference/authentication"
        ],
        "select_paths": [
            r"/reference/authentication.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "campaign_monitor": {
        "domains": ["www.campaignmonitor.com", "developers.createsend.com"],
        "seeds": ["https://developers.createsend.com/docs/oauth/"],
        "select_paths": [
            r"/docs/oauth/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "getresponse": {
        "domains": ["apireference.getresponse.com"],
        "seeds": [
            "https://apireference.getresponse.com/#section/Authentication"
        ],
        "select_paths": [
            r"/#section/Authentication.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "brevo": {
        "domains": ["developers.brevo.com"],
        "seeds": [
            "https://developers.brevo.com/reference/authentication"
        ],
        "select_paths": [
            r"/reference/authentication.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "klaviyo": {
        "domains": ["developers.klaviyo.com"],
        "seeds": ["https://developers.klaviyo.com/en/docs/oauth"],
        "select_paths": [
            r"/en/docs/oauth.*",
            r"/en/docs/.*",
            r"/en/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "kit": {
        "domains": ["developers.kit.com"],
        "seeds": ["https://developers.kit.com/v4/#authentication"],
        "select_paths": [
            r"/v4/#authentication.*",
            r"/v4/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "drip": {
        "domains": ["developer.drip.com"],
        "seeds": ["https://developer.drip.com/#authentication"],
        "select_paths": [
            r"/#authentication.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "mailerlite": {
        "domains": ["developers.mailerlite.com"],
        "seeds": [
            "https://developers.mailerlite.com/api-reference/#authentication"
        ],
        "select_paths": [
            r"/api-reference/#authentication.*",
            r"/api-reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "emma": {
        "domains": ["developer.myemma.com"],
        "seeds": ["https://developer.myemma.com/#authentication"],
        "select_paths": [
            r"/#authentication.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "buffer": {
        "domains": ["buffer.com", "developers.buffer.com"],
        "seeds": ["https://developers.buffer.com/api/"],
        "select_paths": [
            r"/api/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "hootsuite": {
        "domains": ["developer.hootsuite.com"],
        "seeds": ["https://developer.hootsuite.com/docs/oauth"],
        "select_paths": [
            r"/docs/oauth.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "sprout_social": {
        "domains": ["developers.sproutsocial.com"],
        "seeds": ["https://developers.sproutsocial.com/docs/oauth"],
        "select_paths": [
            r"/docs/oauth.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "bitly": {
        "domains": ["dev.bitly.com"],
        "seeds": [
            "https://dev.bitly.com/docs/getting-started/authentication/"
        ],
        "select_paths": [
            r"/docs/getting-started/authentication/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "unbounce": {
        "domains": ["developer.unbounce.com"],
        "seeds": ["https://developer.unbounce.com/api/"],
        "select_paths": [
            r"/api/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "instapage": {
        "domains": ["developers.instapage.com"],
        "seeds": [
            "https://developers.instapage.com/docs/authentication"
        ],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "unleashed": {
        "domains": ["developer.unleashedsoftware.com"],
        "seeds": ["https://developer.unleashedsoftware.com/"],
        "select_paths": [
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "intuit_quickbooks": {
        "domains": ["developer.intuit.com", "developer.qbo.intuit.com"],
        "seeds": [
            "https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0"
        ],
        "select_paths": [
            r"/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2\.0.*",
            r"/app/developer/qbo/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|community|pricing|release-notes).*",
        ],
    },
    "xero": {
        "domains": ["developer.xero.com"],
        "seeds": [
            "https://developer.xero.com/documentation/guides/oauth2/auth-flow"
        ],
        "select_paths": [
            r"/documentation/guides/oauth2/auth-flow.*",
            r"/documentation/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "freshbooks": {
        "domains": ["api.freshbooks.com", "developers.freshbooks.com"],
        "seeds": ["https://api.freshbooks.com/documentation"],
        "select_paths": [
            r"/documentation.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "wave": {
        "domains": ["developer.waveapps.com"],
        "seeds": [
            "https://developer.waveapps.com/hc/en-us/articles/360019764851"
        ],
        "select_paths": [
            r"/hc/en-us/articles/360019764851.*",
            r"/hc/en-us/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "sage": {
        "domains": ["developer.sage.com"],
        "seeds": [
            "https://developer.sage.com/uk/accounting/guides/authentication/"
        ],
        "select_paths": [
            r"/uk/accounting/guides/authentication/.*",
            r"/uk/accounting/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "exact": {
        "domains": [
            "support.exactonline.com",
            "developer.exactonline.com"
        ],
        "seeds": [
            "https://support.exactonline.com/community/s/knowledge_base#id=2137"
        ],
        "select_paths": [
            r"/community/s/knowledge_base#id=2137.*",
            r"/community/s/knowledge_base.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community-events).*",
        ],
    },
    "freeagent": {
        "domains": ["dev.freeagent.com"],
        "seeds": ["https://dev.freeagent.com/docs/oauth"],
        "select_paths": [
            r"/docs/oauth.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "myob": {
        "domains": ["developer.myob.com"],
        "seeds": [
            "https://developer.myob.com/api/accountright/api-guides/authentication/"
        ],
        "select_paths": [
            r"/api/accountright/api-guides/authentication/.*",
            r"/api/accountright/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "fortnox": {
        "domains": ["developer.fortnox.se"],
        "seeds": ["https://developer.fortnox.se/documentation/"],
        "select_paths": [
            r"/documentation/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "visma": {
        "domains": ["developer.visma.com", "docs.visma.com"],
        "seeds": ["https://developer.visma.com/docs/authentication/"],
        "select_paths": [
            r"/docs/authentication/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "datev": {
        "domains": ["developer.datev.de", "www.datev.de"],
        "seeds": ["https://developer.datev.de/"],
        "select_paths": [
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "pennylane": {
        "domains": ["developers.pennylane.com"],
        "seeds": [
            "https://developers.pennylane.com/reference/authentication"
        ],
        "select_paths": [
            r"/reference/authentication.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "brex": {
        "domains": ["developer.brex.com"],
        "seeds": ["https://developer.brex.com/docs/authentication/"],
        "select_paths": [
            r"/docs/authentication/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "ramp": {
        "domains": ["docs.ramp.com"],
        "seeds": [
            "https://docs.ramp.com/developer-api/reference/authentication"
        ],
        "select_paths": [
            r"/developer-api/reference/authentication.*",
            r"/developer-api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "bill": {
        "domains": ["developer.bill.com"],
        "seeds": [
            "https://developer.bill.com/api-documentation/authentication"
        ],
        "select_paths": [
            r"/api-documentation/authentication.*",
            r"/api-documentation/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "expensify": {
        "domains": ["integrations.expensify.com"],
        "seeds": [
            "https://integrations.expensify.com/Integration-Server/doc/"
        ],
        "select_paths": [
            r"/Integration-Server/doc/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "sap_concur": {
        "domains": ["developer.concur.com"],
        "seeds": [
            "https://developer.concur.com/api-reference/authentication/getting-started/oauth-20.html"
        ],
        "select_paths": [
            r"/api-reference/authentication/getting-started/oauth-20\.html.*",
            r"/api-reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "square": {
        "domains": ["developer.squareup.com"],
        "seeds": [
            "https://developer.squareup.com/docs/oauth-api/overview"
        ],
        "select_paths": [
            r"/docs/oauth-api/overview.*",
            r"/docs/oauth-api/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community|release-notes).*",
        ],
    },
    "sumup": {
        "domains": ["developer.sumup.com"],
        "seeds": ["https://developer.sumup.com/docs/oauth"],
        "select_paths": [
            r"/docs/oauth.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "coinbase": {
        "domains": [
            "docs.cdp.coinbase.com",
            "developers.coinbase.com"
        ],
        "seeds": [
            "https://docs.cdp.coinbase.com/coinbase-app/docs/oauth2"
        ],
        "select_paths": [
            r"/coinbase-app/docs/oauth2.*",
            r"/coinbase-app/docs/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "bigcommerce": {
        "domains": ["developer.bigcommerce.com"],
        "seeds": [
            "https://developer.bigcommerce.com/docs/integrations/apis/authentication"
        ],
        "select_paths": [
            r"/docs/integrations/apis/authentication.*",
            r"/docs/integrations/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "woocommerce": {
        "domains": ["developer.wordpress.org", "woocommerce.com"],
        "seeds": [
            "https://developer.wordpress.org/plugins/wordpress-org/"
        ],
        "select_paths": [
            r"/plugins/wordpress-org/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "wix": {
        "domains": ["dev.wix.com"],
        "seeds": [
            "https://dev.wix.com/docs/build-apps/develop-your-app/access-the-wix-app-apis/authentication"
        ],
        "select_paths": [
            r"/docs/build-apps/develop-your-app/access-the-wix-app-apis/authentication.*",
            r"/docs/build-apps/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "squarespace": {
        "domains": ["developers.squarespace.com"],
        "seeds": ["https://developers.squarespace.com/oauth-2-tutorial"],
        "select_paths": [
            r"/oauth-2-tutorial.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "webflow": {
        "domains": ["developers.webflow.com"],
        "seeds": ["https://developers.webflow.com/data/reference/oauth"],
        "select_paths": [
            r"/data/reference/oauth.*",
            r"/data/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "wordpress_com": {
        "domains": ["developer.wordpress.com"],
        "seeds": ["https://developer.wordpress.com/docs/api/oauth2/"],
        "select_paths": [
            r"/docs/api/oauth2/.*",
            r"/docs/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "ebay": {
        "domains": ["developer.ebay.com"],
        "seeds": [
            "https://developer.ebay.com/api-docs/static/oauth-tokens.html"
        ],
        "select_paths": [
            r"/api-docs/static/oauth-tokens\.html.*",
            r"/api-docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "etsy": {
        "domains": ["developers.etsy.com"],
        "seeds": [
            "https://developers.etsy.com/documentation/essentials/authentication"
        ],
        "select_paths": [
            r"/documentation/essentials/authentication.*",
            r"/documentation/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "walmart": {
        "domains": ["developer.walmart.com"],
        "seeds": [
            "https://developer.walmart.com/doc/guides/credentials/"
        ],
        "select_paths": [
            r"/doc/guides/credentials/.*",
            r"/doc/guides/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "mercado_libre": {
        "domains": ["developers.mercadolibre.com"],
        "seeds": [
            "https://developers.mercadolibre.com/en_us/authorization-and-authentication"
        ],
        "select_paths": [
            r"/en_us/authorization-and-authentication.*",
            r"/en_us/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "lightspeed": {
        "domains": ["developers.lightspeedhq.com"],
        "seeds": [
            "https://developers.lightspeedhq.com/retail/introduction/authentication/"
        ],
        "select_paths": [
            r"/retail/introduction/authentication/.*",
            r"/retail/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "clover": {
        "domains": ["docs.clover.com", "developer.clover.com"],
        "seeds": ["https://docs.clover.com/docs/oauth-authentication"],
        "select_paths": [
            r"/docs/oauth-authentication.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "ecwid": {
        "domains": ["developers.ecwid.com"],
        "seeds": [
            "https://developers.ecwid.com/api-documentation/authentication"
        ],
        "select_paths": [
            r"/api-documentation/authentication.*",
            r"/api-documentation/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "vendasta": {
        "domains": ["developers.vendasta.com"],
        "seeds": [
            "https://developers.vendasta.com/reference/authentication"
        ],
        "select_paths": [
            r"/reference/authentication.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "shipstation": {
        "domains": ["www.shipstation.com", "developers.shipstation.com"],
        "seeds": [
            "https://www.shipstation.com/docs/api/authentication/"
        ],
        "select_paths": [
            r"/docs/api/authentication/.*",
            r"/docs/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "shippo": {
        "domains": ["goshippo.com", "developers.goshippo.com"],
        "seeds": ["https://developers.goshippo.com/docs/"],
        "select_paths": [
            r"/docs/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "printful": {
        "domains": ["developers.printful.com"],
        "seeds": ["https://developers.printful.com/docs/"],
        "select_paths": [
            r"/docs/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "printify": {
        "domains": ["developers.printify.com"],
        "seeds": ["https://developers.printify.com/"],
        "select_paths": [
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "cin7": {
        "domains": ["developer.cin7.com"],
        "seeds": ["https://developer.cin7.com/docs/api/authentication"],
        "select_paths": [
            r"/docs/api/authentication.*",
            r"/docs/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "katana": {
        "domains": ["developer.katanamrp.com"],
        "seeds": [
            "https://developer.katanamrp.com/reference/authentication"
        ],
        "select_paths": [
            r"/reference/authentication.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "digitalocean": {
        "domains": ["docs.digitalocean.com"],
        "seeds": ["https://docs.digitalocean.com/reference/api/oauth/"],
        "select_paths": [
            r"/reference/api/oauth/.*",
            r"/reference/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "vercel": {
        "domains": ["vercel.com", "docs.vercel.com"],
        "seeds": [
            "https://vercel.com/docs/integrations/create-integration"
        ],
        "select_paths": [
            r"/docs/integrations/create-integration.*",
            r"/docs/integrations/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community|changelog).*",
        ],
    },
    "netlify": {
        "domains": ["docs.netlify.com", "open-api.netlify.com"],
        "seeds": ["https://docs.netlify.com/api/get-started/"],
        "select_paths": [
            r"/api/get-started/.*",
            r"/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "heroku": {
        "domains": ["devcenter.heroku.com"],
        "seeds": ["https://devcenter.heroku.com/articles/oauth"],
        "select_paths": [
            r"/articles/oauth.*",
            r"/articles/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "render": {
        "domains": ["docs.render.com", "api-docs.render.com"],
        "seeds": ["https://api-docs.render.com/"],
        "select_paths": [
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "sentry": {
        "domains": ["docs.sentry.io", "develop.sentry.dev"],
        "seeds": [
            "https://develop.sentry.dev/integrations/oauth/"
        ],
        "select_paths": [
            r"/integrations/oauth/.*",
            r"/integrations/.*",
            r"/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community|changelog).*",
        ],
    },
    "datadog": {
        "domains": ["docs.datadoghq.com"],
        "seeds": ["https://docs.datadoghq.com/api/latest/"],
        "select_paths": [
            r"/api/latest/.*",
            r"/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community|release-notes).*",
        ],
    },
    "new_relic": {
        "domains": ["developer.newrelic.com", "docs.newrelic.com"],
        "seeds": [
            "https://developer.newrelic.com/build-on-new-relic-api/"
        ],
        "select_paths": [
            r"/build-on-new-relic-api/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "pagerduty": {
        "domains": ["developer.pagerduty.com"],
        "seeds": ["https://developer.pagerduty.com/docs/oauth/"],
        "select_paths": [
            r"/docs/oauth/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "servicenow": {
        "domains": [
            "developer.servicenow.com",
            "docs.servicenow.com"
        ],
        "seeds": [
            "https://developer.servicenow.com/dev.do#!/reference/api/"
        ],
        "select_paths": [
            r"/dev.do#!/reference/api/.*",
            r"/dev.do.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "linear": {
        "domains": ["developers.linear.app", "docs.linear.app"],
        "seeds": [
            "https://developers.linear.app/docs/oauth/authentication"
        ],
        "select_paths": [
            r"/docs/oauth/authentication.*",
            r"/docs/oauth/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "aha": {
        "domains": ["www.aha.io", "support.aha.io"],
        "seeds": ["https://support.aha.io/api/"],
        "select_paths": [
            r"/api/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "productboard": {
        "domains": ["developer.productboard.com"],
        "seeds": [
            "https://developer.productboard.com/reference/authentication"
        ],
        "select_paths": [
            r"/reference/authentication.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "shortcut": {
        "domains": ["developer.shortcut.com"],
        "seeds": ["https://developer.shortcut.com/api/rest-v3"],
        "select_paths": [
            r"/api/rest-v3.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "assembla": {
        "domains": ["developers.assembla.com"],
        "seeds": ["https://developers.assembla.com/"],
        "select_paths": [
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "contentful": {
        "domains": ["contentful.com", "www.contentful.com"],
        "seeds": [
            "https://www.contentful.com/developers/docs/references/authentication/"
        ],
        "select_paths": [
            r"/developers/docs/references/authentication/.*",
            r"/developers/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "contentstack": {
        "domains": ["www.contentstack.com", "devdocs.contentstack.com"],
        "seeds": [
            "https://www.contentstack.com/docs/developers/create-stack-tokens/"
        ],
        "select_paths": [
            r"/docs/developers/create-stack-tokens/.*",
            r"/docs/developers/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "sanity": {
        "domains": ["www.sanity.io"],
        "seeds": [
            "https://www.sanity.io/docs/content-lake/http-auth"
        ],
        "select_paths": [
            r"/docs/content-lake/http-auth.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "snowflake": {
        "domains": ["docs.snowflake.com"],
        "seeds": [
            "https://docs.snowflake.com/en/user-guide/oauth-intro"
        ],
        "select_paths": [
            r"/en/user-guide/oauth-intro.*",
            r"/en/user-guide/.*",
            r"/en/developer-guide/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community|release-notes).*",
        ],
    },
    "autodesk": {
        "domains": ["aps.autodesk.com", "developer.autodesk.com"],
        "seeds": ["https://aps.autodesk.com/en/docs/oauth/v2/"],
        "select_paths": [
            r"/en/docs/oauth/v2/.*",
            r"/en/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "cisco_webex": {
        "domains": ["developer.webex.com", "help.webex.com"],
        "seeds": ["https://developer.webex.com/docs/integrations"],
        "select_paths": [
            r"/docs/integrations.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "ringcentral": {
        "domains": ["developers.ringcentral.com"],
        "seeds": [
            "https://developers.ringcentral.com/guide/authentication/oauth/authorization-code"
        ],
        "select_paths": [
            r"/guide/authentication/oauth/authorization-code.*",
            r"/guide/authentication/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "dialpad": {
        "domains": ["developers.dialpad.com"],
        "seeds": [
            "https://developers.dialpad.com/docs/authentication"
        ],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "aircall": {
        "domains": ["developer.aircall.io"],
        "seeds": [
            "https://developer.aircall.io/docs/authentication"
        ],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "8x8": {
        "domains": ["developer.8x8.com", "support.8x8.com"],
        "seeds": ["https://developer.8x8.com/"],
        "select_paths": [
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "goto": {
        "domains": ["developer.goto.com", "support.goto.com"],
        "seeds": [
            "https://developer.goto.com/guides/authentication/"
        ],
        "select_paths": [
            r"/guides/authentication/.*",
            r"/guides/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "discord": {
        "domains": ["discord.com", "discord.com/developers"],
        "seeds": [
            "https://docs.discord.com/developers/topics/oauth2"
        ],
        "select_paths": [
            r"/developers/topics/oauth2.*",
            r"/developers/topics/.*",
            r"/developers/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "reddit": {
        "domains": [
            "support.reddithelp.com",
            "www.reddit.com/dev/api"
        ],
        "seeds": [
            "https://support.reddithelp.com/hc/en-us/articles/16160319875092"
        ],
        "select_paths": [
            r"/hc/en-us/articles/16160319875092.*",
            r"/hc/en-us/.*",
            r"/dev/api.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "x": {
        "domains": ["developer.x.com", "docs.x.com"],
        "seeds": [
            "https://docs.x.com/resources/fundamentals/authentication/oauth-2-0"
        ],
        "select_paths": [
            r"/resources/fundamentals/authentication/oauth-2-0.*",
            r"/resources/fundamentals/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "pinterest": {
        "domains": ["developers.pinterest.com"],
        "seeds": [
            "https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/"
        ],
        "select_paths": [
            r"/docs/getting-started/set-up-authentication-and-authorization/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "tiktok": {
        "domains": ["developers.tiktok.com"],
        "seeds": [
            "https://developers.tiktok.com/doc/oauth-user-access-token-management"
        ],
        "select_paths": [
            r"/doc/oauth-user-access-token-management.*",
            r"/doc/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "snapchat": {
        "domains": ["developers.snap.com"],
        "seeds": [
            "https://developers.snap.com/api/marketing-api/Ads-API/oauth"
        ],
        "select_paths": [
            r"/api/marketing-api/Ads-API/oauth.*",
            r"/api/marketing-api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "line": {
        "domains": ["developers.line.biz"],
        "seeds": [
            "https://developers.line.biz/en/docs/line-login/integrate-line-login/"
        ],
        "select_paths": [
            r"/en/docs/line-login/integrate-line-login/.*",
            r"/en/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "kakao": {
        "domains": ["developers.kakao.com"],
        "seeds": [
            "https://developers.kakao.com/docs/en/kakaologin/common"
        ],
        "select_paths": [
            r"/docs/en/kakaologin/common.*",
            r"/docs/en/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "wechat": {
        "domains": ["developers.weixin.qq.com"],
        "seeds": [
            "https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html"
        ],
        "select_paths": [
            r"/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization\.html.*",
            r"/doc/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "gusto": {
        "domains": ["docs.gusto.com"],
        "seeds": [
            "https://docs.gusto.com/embedded-payroll/docs/api-access/authentication"
        ],
        "select_paths": [
            r"/embedded-payroll/docs/api-access/authentication.*",
            r"/embedded-payroll/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "bamboohr": {
        "domains": ["documentation.bamboohr.com"],
        "seeds": [
            "https://documentation.bamboohr.com/reference/authentication"
        ],
        "select_paths": [
            r"/reference/authentication.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "deel": {
        "domains": ["developer.deel.com"],
        "seeds": [
            "https://developer.deel.com/docs/authentication"
        ],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "deputy": {
        "domains": ["developer.deputy.com"],
        "seeds": [
            "https://developer.deputy.com/reference/authentication"
        ],
        "select_paths": [
            r"/reference/authentication.*",
            r"/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "bullhorn": {
        "domains": ["bullhorn.github.io", "developer.bullhorn.com"],
        "seeds": [
            "https://bullhorn.github.io/rest-api-docs/restapireference.html"
        ],
        "select_paths": [
            r"/rest-api-docs/restapireference\.html.*",
            r"/rest-api-docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "canva": {
        "domains": ["www.canva.dev", "www.canva.com"],
        "seeds": ["https://www.canva.dev/docs/apps/oauth/"],
        "select_paths": [
            r"/docs/apps/oauth/.*",
            r"/docs/apps/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "figma": {
        "domains": ["www.figma.com", "developers.figma.com"],
        "seeds": ["https://www.figma.com/developers/api#oauth2"],
        "select_paths": [
            r"/developers/api#oauth2.*",
            r"/developers/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "spotify": {
        "domains": ["developer.spotify.com"],
        "seeds": [
            "https://developer.spotify.com/documentation/web-api/concepts/authorization"
        ],
        "select_paths": [
            r"/documentation/web-api/concepts/authorization.*",
            r"/documentation/web-api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "twitch": {
        "domains": ["dev.twitch.tv"],
        "seeds": [
            "https://dev.twitch.tv/docs/authentication/"
        ],
        "select_paths": [
            r"/docs/authentication/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "vimeo": {
        "domains": ["developer.vimeo.com"],
        "seeds": [
            "https://developer.vimeo.com/api/authentication"
        ],
        "select_paths": [
            r"/api/authentication.*",
            r"/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "dailymotion": {
        "domains": ["developers.dailymotion.com"],
        "seeds": ["https://developers.dailymotion.com/api/"],
        "select_paths": [
            r"/api/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "soundcloud": {
        "domains": ["developers.soundcloud.com"],
        "seeds": [
            "https://developers.soundcloud.com/docs/api/explorer"
        ],
        "select_paths": [
            r"/docs/api/explorer.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "deezer": {
        "domains": ["developers.deezer.com"],
        "seeds": ["https://developers.deezer.com/api/oauth"],
        "select_paths": [
            r"/api/oauth.*",
            r"/api/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "tidal": {
        "domains": ["developer.tidal.com"],
        "seeds": [
            "https://developer.tidal.com/documentation/api/authentication"
        ],
        "select_paths": [
            r"/documentation/api/authentication.*",
            r"/documentation/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "patreon": {
        "domains": ["docs.patreon.com"],
        "seeds": ["https://docs.patreon.com/#oauth"],
        "select_paths": [
            r"/#oauth.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "strava": {
        "domains": ["developers.strava.com"],
        "seeds": [
            "https://developers.strava.com/docs/authentication/"
        ],
        "select_paths": [
            r"/docs/authentication/.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "fitbit": {
        "domains": ["dev.fitbit.com"],
        "seeds": [
            "https://dev.fitbit.com/build/reference/web-api/authorization/"
        ],
        "select_paths": [
            r"/build/reference/web-api/authorization/.*",
            r"/build/reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "withings": {
        "domains": ["developer.withings.com"],
        "seeds": [
            "https://developer.withings.com/api-reference/#tag/oauth2"
        ],
        "select_paths": [
            r"/api-reference/#tag/oauth2.*",
            r"/api-reference/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "oura": {
        "domains": ["cloud.ouraring.com", "support.ouraring.com"],
        "seeds": [
            "https://cloud.ouraring.com/docs/authentication"
        ],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "whoop": {
        "domains": ["developer.whoop.com"],
        "seeds": [
            "https://developer.whoop.com/docs/authentication"
        ],
        "select_paths": [
            r"/docs/authentication.*",
            r"/docs/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "polar": {
        "domains": [
            "www.polaraccesslink.com",
            "www.polar.com"
        ],
        "seeds": [
            "https://www.polaraccesslink.com/#section/Authentication"
        ],
        "select_paths": [
            r"/#section/Authentication.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "garmin": {
        "domains": ["developer.garmin.com"],
        "seeds": [
            "https://developer.garmin.com/connect-iq/api-guide/"
        ],
        "select_paths": [
            r"/connect-iq/api-guide/.*",
            r"/connect-iq/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "coros": {
        "domains": ["open.coros.com"],
        "seeds": ["https://open.coros.com/"],
        "select_paths": [
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "concept2": {
        "domains": [
            "log.concept2.com",
            "developer.concept2.com"
        ],
        "seeds": [
            "https://log.concept2.com/developers/documentation/"
        ],
        "select_paths": [
            r"/developers/documentation/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
    "peloton": {
        "domains": ["peloton.github.io", "www.onepeloton.com"],
        "seeds": [
            "https://peloton.github.io/api-docs/"
        ],
        "select_paths": [
            r"/api-docs/.*",
            r"/.*",
        ],
        "exclude_paths": [
            r".*/(blog|pricing|community).*",
        ],
    },
}