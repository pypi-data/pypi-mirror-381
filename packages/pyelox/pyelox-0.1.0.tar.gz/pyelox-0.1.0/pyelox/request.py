import urllib.parse

class PyEloxRequest:
    def __init__(self, raw_request):
        self.raw_request = raw_request
        self.headers = {}
        self.method = None
        self.path = None
        self.body = None
        self.form_data = {}
        self.url_vars = {}
        self._parse_request()

    def _parse_request(self):
        lines = self.raw_request.split('\r\n')
        if not lines:
            return

        first_line = lines[0].split()
        if len(first_line) >= 3:
            self.method = first_line[0]
            path_with_query = first_line[1]
            
            if '?' in path_with_query:
                self.path, query_string = path_with_query.split('?', 1)
                self.query_params = dict(urllib.parse.parse_qsl(query_string))
            else:
                self.path = path_with_query
                self.query_params = {}

        header_end_index = lines.index('') if '' in lines else -1
        
        for line in lines[1:header_end_index]:
            if ': ' in line:
                key, value = line.split(': ', 1)
                self.headers[key.lower()] = value
        
        if header_end_index != -1:
            self.body = '\r\n'.join(lines[header_end_index + 1:])
            
            if self.method == 'POST':
                if 'content-type' in self.headers and 'application/x-www-form-urlencoded' in self.headers['content-type']:
                    self.form_data = dict(urllib.parse.parse_qsl(self.body))

    def get_form(self, key, default=None):
        return self.form_data.get(key, default)

    def get_query(self, key, default=None):
        return self.query_params.get(key, default)