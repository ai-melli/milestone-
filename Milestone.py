import pandas as pd
from datetime import datetime
try:
    def get_user_input():
        projects = []
        while True:
            project_name = input("Enter your project name or 'done' to finish: ")
            if project_name.lower() == 'done':
                break
            milestone = input("Enter milestone: ")
            completion_date = input("Enter completion date (YYYY-MM-DD): ")
            planned_date = input("Enter planned date (YYYY-MM-DD): ")
            status = input("Enter status (Completed or Not Completed): ")

            project = {
                "Project Name": project_name,
                "Milestone": milestone,
                "Completed Date": completion_date,
                "Planned Date": planned_date,
                "Status": status
            }
            projects.append(project)
        
        return projects

    def is_on_track(milestone):
        if milestone['Status'].lower() == 'completed':
            completion_date = datetime.strptime(milestone['Completed Date'], '%Y-%m-%d')
            planned_date = datetime.strptime(milestone['Planned Date'], '%Y-%m-%d')
            if completion_date <= planned_date:
                return 'On Track'
            return 'Not on Track'

    def main():
        projects = get_user_input()
        
        
        df = pd.DataFrame(projects)
        
        
        df['On Track'] = df.apply(is_on_track, axis=1)
        
        # Display DataFrame
        print("\nMilestone Status:")
        print(df)

    if __name__ == "__main__":
        main()
except :
    print("An error occured")

