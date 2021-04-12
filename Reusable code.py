import pandas as pd


# Importing and Inital Review of Data: employee_survey
def import_data(filename):
    data = pd.read_csv(filename)
    print(data)
    print(data.head())
    print(data.info())
    print(data.describe())
    print(data.shape)
    print(data.columns)
    print(data.index)
    return data


data = import_data("XYZ Company/employee_survey_data.csv")


# Analysing Data: employee_survey
# Sorting employee_survey from lowest to highest
def sort_values(columns):
    employee_survey_dataset = data.sort_values(columns)
    print(employee_survey_dataset.head())


sort_values(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])

# Importing and Inital Review of Data: manager_survey
data = import_data("XYZ Company/manager_survey_data.csv")

# Analysing Data: manager survey
# Sorting manager survey from lowest to highest
sort_values(["JobInvolvement", "PerformanceRating"])

# Importing and Inital Review of Data: general_data
data = import_data("XYZ Company/general_data.csv")

# Rename Columns
def rename(column):
    rename = data.rename(columns={column: "EducationLevel"}, inplace=True)
    print(rename)
    return data


# Print out the mean of np_height_in - numpy
print(np.mean(np_height_in))
# Print out the median of np_height_in
print(np.median(np_height_in))
# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))
# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))
# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))
# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr

# Subsetting by row/column number
def iloc(row,column):
    iloc = print(data.iloc[row,column])
    print(iloc)
    return data

#The below works - tried making it better on other page to use again for If statements and Numpy
data["JobInvolvement"] = data["JobInvolvement"].replace({1: "Low", 2: "Medium", 3: "High", 4: "Very High"})
data["PerformanceRating"] = data["PerformanceRating"].replace({1: "Low", 2: "Good", 3: "Excellent", 4: "Outstanding"})

# Merge Data Code when fixed - add when FIXED
df1 = pd.merge(employee_survey_data, general_data, how="inner", on="EmployeeID")
data = pd.merge(manager_survey_data, general_data, how="inner", on="EmployeeID")
#This works
my_dict_manager_survey2 = dict({1: "Low", 2: "Good", 3: "Excellent", 4: "Outstanding"})
data["PerformanceRating"] = data["PerformanceRating"].replace(my_dict_manager_survey2)
print(data.head())
#Fix this
my_dict_general_data1 = dict({1: "Below College", 2: "College", 3: "Bachelor", 4: "Master", 5: "Doctor"})
data["Education_Level"] = data["Education_Level"].replace(my_dict_general_data1)
print(data.head())

# need to create a list to do it - test without list
csv = np.genfromtxt ("XYZ Company/general_data.csv", delimiter=",")
data.to_numpy()
BusinessTravel = ("Non-Travel", "Travel_Rarely", "Travel_Frequently")
Attrition = ("Yes", "No")
np_BusinessTravel = np.array("BusinessTravel")
np_Attrition = np.array("Attrition")
np_travel_attrition = np_BusinessTravel[np_Attrition == 'Yes']
value_counts(np_travel_attrition)
print(np_Attrition)
#education field, job level, college

value_counts_number = data["NumCompaniesWorked"].value_counts(ascending=False)
print(value_counts_number)

#seaborn & matplotlib
#Environment Sat and Attrition
sns.countplot(x = "Attrition",data=general_data,hue="Gender")
plt.show()

# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender", y="Age", data=survey_data, kind="bar")
# Show plot
plt.show()

# or

# Set palette to "Blues"
sns.set_palette("Blues")
# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data,
                kind="box", hue="Attrition")
# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Attrition by Demographics")
# Show plot
plt.show()

plt.figure(figsize=(8,8))
sns.violinplot(y='Age',x='Attrition',data=hr)
plt.show()

plt.figure(figsize=(8,10))
ax = sns.countplot(x='EnvironmentSatisfaction', data=general_data, hue="Attrition")
ax.set_ylabel('# of Employee')
bars = ax.patches
half = int(len(bars)/2)
left_bars = bars[:half]
right_bars = bars[half:]

for left, right in zip(left_bars, right_bars):
    height_l = left.get_height()
    height_r = right.get_height()
    total = height_l + height_r

    ax.text(left.get_x() + left.get_width()/2., height_l + 30, '{0:.0%}'.format(height_l/total), ha="center")
    ax.text(right.get_x() + right.get_width()/2., height_r + 40, '{0:.0%}'.format(height_r/total), ha="center")

plt.figure(figsize=(8,8))
ax = sns.countplot(x='JobSatisfaction', data=general_data, hue="Attrition")
ax.set_ylabel('# of Employee')
bars = ax.patches
half = int(len(bars)/2)
left_bars = bars[:half]
right_bars = bars[half:]

for left, right in zip(left_bars, right_bars):
    height_l = left.get_height()
    height_r = right.get_height()
    total = height_l + height_r

    ax.text(left.get_x() + left.get_width()/2., height_l + 40, '{0:.0%}'.format(height_l/total), ha="center")
    ax.text(right.get_x() + right.get_width()/2., height_r + 40, '{0:.0%}'.format(height_r/total), ha="center")

# Change the orientation of the plot
# Create column subplots based on age category
sns.catplot(y="Department", data=survey_data,
            kind="count", col="Age")
# Show plot
plt.show()

def pie(category):
    label = []
    label_percent = []
    for cat in general_df[category].unique():
        label.append(cat)
        t1 = general_df[(general_df[category] == cat) & (general_df['Attrition'] == 'Yes')].shape[0]
        t2 = general_df[general_df[category] == cat].shape[0]
        label_percent.append(t1/t2 * 100)
    fig1, ax1 = plt.subplots()
    ax1.pie(label_percent, labels=label, autopct='%1.1f%%', shadow=True, startangle=180)
    centre_circle = plt.Circle((0,0),0.75,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.title(category)
    plt.show()

pie("Education")
pie("Department")
pie('BusinessTravel')
#As obeserved earlier people from HR background has high tendency to leave.
#From the above graph it seems like company need to check its policy on travelling as almost 83% people who travels has a tendency to leave Among them frequent travellers has a higher possibility of leaving the company.
#https://www.kaggle.com/priyam6792/hr-case-study
