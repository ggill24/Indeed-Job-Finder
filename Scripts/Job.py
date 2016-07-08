class Job:

    job_title = None
    job_url = None

    def __init__(self, title, url):

        self.job_title = title
        self.job_url = url



    def title(self):
        return self.job_title

    def url(self):
        return self.job_url