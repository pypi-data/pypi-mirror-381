from ap_health_report import generate_ap_health_report

def test_runs(tmp_path):
    log_content = "CPU Usage: 40%\nMemory Usage: 30%\nerror\nwarning\nfail"
    log_path = tmp_path / "log.txt"
    log_path.write_text(log_content)
    results = generate_ap_health_report(str(log_path), print_report=False)
    assert "cpu_health" in results
    assert "error_counts" in results
