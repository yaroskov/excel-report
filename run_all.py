import config
from classes.make_tasks.MakeTasksRun import MakeTasksRun
from classes.excel_report.CreationRun import CreationRun
from classes.report.BeautyReportRun import ReportRun


tasks = MakeTasksRun(config)
tasks.run()
config.paths["tasks"]["list"] = tasks.file_name

report_data = CreationRun(config)
report_data.run_fully()
config.paths["results"]["ready"] = report_data.results_lite_file_name

report = ReportRun(config)
report.run()
