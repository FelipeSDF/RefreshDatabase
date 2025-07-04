from automate import MagniFinanceControl, QuickBooksControl

control = QuickBooksControl('https://accounts.intuit.com/app/sign-in?app_group=QBO&asset_alias=Intuit.accounting.core.qbowebapp&locale=en-ROW&state=%7B%22queryParams%22%3A%7B%22locale%22%3A%22en-ROW%22%7D%7D&app_environment=prod&origin-server=bff')
process = control.automateAll()

control = MagniFinanceControl('https://portal.magnifinance.com/Login?originalURL=https%3A%2F%2Fportal.magnifinance.com%2FPivot')
control.automateAll()
