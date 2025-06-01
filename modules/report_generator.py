import os
import csv
import statistics

def generate_report(data, threshold=2.0, report_path="reports/discrepancy_report.csv"):
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    header = [
        "City",
        "Web Temperature (\u00b0C)",
        "API Temperature (\u00b0C)",
        "Discrepancy (\u00b0C)",
        "Discrepancy (%)"
    ]
    discrepancies = []
    with open(report_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Discrepancy Report"])
        writer.writerow([])
        writer.writerow(header)
        for row in data:
            city, temp_web, _, temp_api, _, _ = row
            diff = abs(temp_web - temp_api)
            percent_diff = (diff / ((temp_web + temp_api) / 2)) * 100 if (temp_web + temp_api) != 0 else 0
            if diff > threshold:
                writer.writerow([
                    city,
                    round(temp_web, 1),
                    round(temp_api, 1),
                    round(diff, 2),
                    f"{round(percent_diff, 1)}%"
                ])
                discrepancies.append(diff)
        writer.writerow([])
        writer.writerow(["Summary Statistics"])
        writer.writerow(["Total Cities Analyzed", len(data)])
        writer.writerow(["Cities Exceeding Threshold", len(discrepancies)])
        if discrepancies:
            writer.writerow(["Mean Discrepancy (\u00b0C)", round(statistics.mean(discrepancies), 2)])
            writer.writerow(["Max Discrepancy (\u00b0C)", round(max(discrepancies), 2)])
            writer.writerow(["Min Discrepancy (\u00b0C)", round(min(discrepancies), 2)])
        else:
            writer.writerow(["No discrepancies exceeded the defined threshold."])
    print(f"Report saved to {report_path}")