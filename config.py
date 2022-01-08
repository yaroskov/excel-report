import config_pseudos
import config_services
import config_unique

# User's configuration of program.

# Options:
options = {
	"usePseudo": True,
	"useServices": True,
}

# Paths to program files and folders:
paths = {
	"results_full": "excel_report/results/full/",
	"results_light": "excel_report/results/light/",
	"results": {
		"ready": "excel_report/results/light/results_light_30-12-2021_03.28.43.json"
	},
	"source": "excel_report/source/2021-12-29-10.00.02_2.htm",
	"report": "report/",
	"tasks": {
		"list": "tasks/results/tasks_27-12-2021_20.05.51.json",
		"source": "tasks/source/jira.egovdev 2021-12-30T18_08_05+0300.html",
		"results": "tasks/results/"
	}
}

# List of pseudonyms:
pseudos = config_pseudos.data

# List of services:
services = config_services.data

# Uniqueization dictionary:
unique = config_unique
