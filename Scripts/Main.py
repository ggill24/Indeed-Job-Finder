from JobSeeker import JobSeeker

def main():
    indeed = JobSeeker("Toronto", "ON", True, "it support", "desktop support", "help desk")
    indeed.search()


if __name__ == "__main__":
    main()
