import requests

class RedashHelper:
    def __init__(self, api_key, redash_url):
        self.api_key = api_key
        self.redash_url = redash_url
        self.headers = {"Authorization": f"Key {api_key}", "Content-Type": "application/json"}

    def create_query(self, name, query, data_source_id):
        api_url = f"{self.redash_url}/api/queries"
        query_data = {
            "name": name,
            "query": query,
            "data_source_id": data_source_id,
        }
        response = requests.post(api_url, headers=self.headers, json=query_data)
        return response.json()["id"] if response.status_code == 200 else None

    def create_table_visualization(self, query_id, columns):
        visualization_data = {
            "name": "Table Visualization",
            "type": "TABLE",
            "query_id": query_id,
            "options": {
                "columns": columns
            }
        }
        return self._create_visualization(visualization_data)

    def create_line_chart_visualization(self, query_id, x_axis, y_axes):
        visualization_data = {
            "type": "CHART",
            "name": "Line Chart",
            "query_id": query_id,
            "options": {
                "globalSeriesType": "line",
                "sortX": True,
                "legend": {"enabled": True},
                "xAxis": {"type": "-", "labels": {"enabled": True}},
                "yAxis": [{"type": "linear", "column": y} for y in y_axes],
                "error_y": {"type": "data", "visible": True},
                "columnMapping": {x_axis: "x", **{y: "y" for y in y_axes}},
                "showDataLabels": False
            }
        }
        return self._create_visualization(visualization_data)

    def create_histogram_visualization(self, query_id,  x_axis, y_axes):
        visualization_data = {
            "type": "CHART",
            "name": "Histogram",
            "query_id": query_id,
            "options": {
                "globalSeriesType": "column",
                "sortX": True,
                "legend": {"enabled": True, "placement": "auto", "traceorder": "normal"},
                "xAxis": {"type": "-", "labels": {"enabled": True}},
                "yAxis": [{"type": "linear"}, {"type": "linear", "opposite": True}],
                "alignYAxesAtZero": False,
                "error_y": {"type": "data", "visible": True},
                "series": {"stacking": None, "error_y": {"type": "data", "visible": True}},
                "columnMapping": {x_axis: "x", **{y: "y" for y in y_axes}},
                "direction": {"type": "counterclockwise"},
            },
        }
        return self._create_visualization(visualization_data)


    def create_pie_chart_visualization(self, query_id,  x_axis, y_axes):
        visualization_data = {
            "type": "CHART",
            "name": "Pie Chart",
            "query_id": query_id,
            "options": {
                "globalSeriesType": "pie",
                "sortX": True,
                "legend": {"enabled": True, "placement": "auto", "traceorder": "normal"},
                "xAxis": {"type": "-", "labels": {"enabled": True}},
                "yAxis": [{"type": "linear"}, {"type": "linear", "opposite": True}],
                "alignYAxesAtZero": False,
                "error_y": {"type": "data", "visible": True},
                "series": {"stacking": None, "error_y": {"type": "data", "visible": True}},
                "columnMapping": {x_axis: "x", **{y: "y" for y in y_axes}},
                "direction": {"type": "counterclockwise"},
            },
        }
        return self._create_visualization(visualization_data)

    def create_scatter_plot_visualization(self, query_id, x_axis, y_axes):
        visualization_data = {
            "type": "CHART",
            "name": "Scatter Plot",
            "query_id": query_id,
            "options": {
                "globalSeriesType": "scatter",
                "sortX": True,
                "legend": {"enabled": True, "placement": "auto", "traceorder": "normal"},
                "xAxis": {"type": "-", "labels": {"enabled": True}},
                "yAxis": [{"type": "linear", "column": y} for y in y_axes],
                "alignYAxesAtZero": False,
                "error_y": {"type": "data", "visible": True},
                "series": {"stacking": None, "error_y": {"type": "data", "visible": True}},
                "columnMapping": {x_axis: "x", **{y: "y" for y in y_axes}},
                "direction": {"type": "counterclockwise"},
            },
        }
        return self._create_visualization(visualization_data)

    def _create_visualization(self, visualization_data):
        try:
            api_url = f"{self.redash_url}/api/visualizations"
            response = requests.post(api_url, headers=self.headers, json=visualization_data)

            if response.status_code == 200:
                visualization_id = response.json()["id"]
                print(f"Visualization created successfully. Visualization ID: {visualization_id}")
                return visualization_id
            else:
                print(f"Failed to create visualization. Status code: {response.status_code}")
                print(response.text)
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error in making the API request: {e}")
            return None

    def create_new_dashboard(self, name):
        try:
            api_url = f"{self.redash_url}/api/dashboards"
            dashboard_data = {
                "name": name,
            }

            response = requests.post(api_url, headers=headers, json=dashboard_data)
            dashboard_slug = response.json()["slug"]
            dashboard_id = response.json()["id"]
            return (dashboard_slug, dashboard_id)
        except requests.exceptions.RequestException as e:
            print(f"Error in creating dashboard {e}")
            return None
    
    def add_visualization_to_dashboard(self, dashboard_id, visualization_id):
        try:
            api_url = f"{self.redash_url}/api/dashboards/{dashboard_id}"

            widget_data = {
                "visualization_id": visualization_id,
                "width": 3,
            }

            response = requests.post(api_url, headers=headers, json=widget_data)
        except requests.exceptions.RequestException as e:
            print(f"Error in adding the visualization. {e}")