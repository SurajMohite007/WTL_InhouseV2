
from flask import Flask, redirect, render_template, request
from pymongo import MongoClient
import pandas as pd
from flask import jsonify
import pdfplumber
import pandas as pd


app = Flask(__name__)

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['your_database']
collection = db['your_collection']

#Colabcode

    # Open the PDF file

@app.route('/')
def homepage():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return 'No file part'

    files = request.files.getlist('file')

    # If the user does not select a file, the browser may submit an empty file without a filename
    if not files:
        return 'No selected file'

    # Iterate through each uploaded file
    for file in files:
        # If the file is present and has a filename
        if file.filename != '':   
            with pdfplumber.open(file) as pdf:
                # Extract the first page
                first_page = pdf.pages[0]

                # Extract all tables from the first page
                tables = first_page.extract_tables()

                # Assuming the table you want is the first one, you can access it like this:
                if tables:
                    table_data = tables[2]
                    # Remove None values and empty strings
                    cleaned_data = [[item for item in row if item is not None and item != ""] for row in table_data]

                    # Convert cleaned data to a DataFrame
                    df = pd.DataFrame(cleaned_data[1:], columns=cleaned_data[0])

                    # Save DataFrame to Excel file
                    df.to_excel('extracted_table1.xlsx', index=False)

                    print("Table extracted and saved to 'extracted_table.xlsx' file successfully.")
                else:
                    print("No tables found on the first page.")

            # Open the PDF file
            with pdfplumber.open(file) as pdf:
                # Extract the first page
                first_page = pdf.pages[1]

                # Extract all tables from the first page
                tables = first_page.extract_tables()

                # Assuming the table you want is the first one, you can access it like this:
                if tables:
                    table_data = tables[2]
                    # Remove None values and empty strings
                    cleaned_data = [[item for item in row if item is not None and item != ""] for row in table_data]

                    # Convert cleaned data to a DataFrame
                    df = pd.DataFrame(cleaned_data[1:], columns=cleaned_data[0])

                    # Save DataFrame to Excel file
                    df.to_excel('extracted_table2.xlsx', index=False)

                    print("Table extracted and saved to 'extracted_table.xlsx' file successfully.")
                else:
                    print("No tables found on the first page.")


            with pdfplumber.open(file) as pdf:
                # Extract the first page
                first_page = pdf.pages[2]

                # Extract all tables from the first page
                tables = first_page.extract_tables()

                # Assuming the table you want is the first one, you can access it like this:
                if tables:
                    table_data = tables[2]
                    # Remove None values and empty strings
                    cleaned_data = [[item for item in row if item is not None and item != ""] for row in table_data]

                    # Convert cleaned data to a DataFrame
                    df = pd.DataFrame(cleaned_data[1:], columns=cleaned_data[0])

                    # Save DataFrame to Excel file
                    df.to_excel('extracted_table3.xlsx', index=False)

                    print("Table extracted and saved to 'extracted_table.xlsx' file successfully.")
                else:
                    print("No tables found on the first page.")

            with pdfplumber.open(file) as pdf:
                # Extract the first page
                first_page = pdf.pages[3]

                # Extract all tables from the first page
                tables = first_page.extract_tables()

                # Assuming the table you want is the first one, you can access it like this:
                if tables:
                    table_data = tables[2]
                    # Remove None values and empty strings
                    cleaned_data = [[item for item in row if item is not None and item != ""] for row in table_data]

                    # Convert cleaned data to a DataFrame
                    df = pd.DataFrame(cleaned_data[1:], columns=cleaned_data[0])

                    # Save DataFrame to Excel file
                    df.to_excel('extracted_table4.xlsx', index=False)

                    print("Table extracted and saved to 'extracted_table.xlsx' file successfully.")
                else:
                    print("No tables found on the first page.") 


            df1 = pd.read_excel('extracted_table1.xlsx')

            # Separate batch name and subject
            df1['Batch'] = df1['SUBJECT'].where(df1['SUBJECT'].str.len() == 2)
            df1['Subject'] = df1['SUBJECT'].where(df1['SUBJECT'].str.len() > 2)

            # Drop the original 'SUBJECT' column
            df1.drop(columns=['SUBJECT'], inplace=True)
            df1['Subject'] = df1['Subject'].fillna(method='ffill')
            df1 = df1.dropna(subset=['Batch'])


            # print(df1)

            df2 = pd.read_excel('extracted_table2.xlsx')

            # Separate batch name and subject
            df2['Batch'] = df2['SUBJECT'].where(df2['SUBJECT'].str.len() == 2)
            df2['Subject'] = df2['SUBJECT'].where(df2['SUBJECT'].str.len() > 2)

            # Drop the original 'SUBJECT' column
            df2.drop(columns=['SUBJECT'], inplace=True)
            df2['Subject'] = df2['Subject'].fillna(method='ffill')
            df2 = df2.dropna(subset=['Batch'])


            # print(df2)
            df3 = pd.read_excel('extracted_table3.xlsx')

            # Separate batch name and subject
            df3['Batch'] = df3['SUBJECT'].where(df3['SUBJECT'].str.len() == 2)
            df3['Subject'] = df3['SUBJECT'].where(df3['SUBJECT'].str.len() > 2)

            # Drop the original 'SUBJECT' column
            df3.drop(columns=['SUBJECT'], inplace=True)
            df3['Subject'] = df3['Subject'].fillna(method='ffill')
            df3 = df3.dropna(subset=['Batch'])


            # print(df3)
            df4 = pd.read_excel('extracted_table4.xlsx')

            # Separate batch name and subject
            df4['Batch'] = df4['SUBJECT'].where(df4['SUBJECT'].str.len() == 2)
            df4['Subject'] = df4['SUBJECT'].where(df4['SUBJECT'].str.len() > 2)

            # Drop the original 'SUBJECT' column
            df4.drop(columns=['SUBJECT'], inplace=True)
            df4['Subject'] = df4['Subject'].fillna(method='ffill')
            df4 = df4.dropna(subset=['Batch'])


            # print(df4)

            # Your four dataframes (df1, df2, df3, df4)
            # Assuming these dataframes are already defined with the given data

            # Concatenate the dataframes
            all_divisions = pd.concat([df1, df2, df3, df4], ignore_index=True)

            # Display the merged dataframe
            # print(all_divisions)

            students_df1 = pd.read_excel("student.xlsx", "TE1", skiprows=2)
            students_df1 = students_df1.loc[:, ~students_df1.columns.str.contains('^Unnamed')]
            students_df1['Batch'] = students_df1['Batch'].fillna(method='ffill')
            students_df1.index = range(1, len(students_df1) + 1)
            students_df1

            students_df2 = pd.read_excel("student.xlsx", "TE2 (2)", skiprows=2)
            students_df2 = students_df2.loc[:, ~students_df2.columns.str.contains('^Unnamed')]
            students_df2['Batch'] = students_df2['Batch'].fillna(method='ffill')
            students_df2.index = range(1, len(students_df2) + 1)
            students_df2

            students_df3 = pd.read_excel("student.xlsx", "TE 3 (3)", skiprows=2)
            students_df3 = students_df3.loc[:, ~students_df3.columns.str.contains('^Unnamed')]
            students_df3['Batch'] = students_df3['Batch'].fillna(method='ffill')
            students_df3.index = range(1, len(students_df3) + 1)
            students_df3

            students_df4 = pd.read_excel("student.xlsx", "TE 4 (4)", skiprows=2)
            students_df4 = students_df4.loc[:, ~students_df4.columns.str.contains('^Unnamed')]
            students_df4['Batch'] = students_df4['Batch'].fillna(method='ffill')
            students_df4.index = range(1, len(students_df4) + 1)
            students_df4

            final = pd.concat([students_df1, students_df2, students_df3, students_df4], ignore_index=True)

            # Display the merged dataframe
            # print(final)

            output_df = pd.merge(all_divisions, final, on='Batch')
            output_df

            # Group by staff name and subject, and count the number of students
            # Group by 'STAFF', 'Subject', 'Batch', and count the number of students
            grouped_data = output_df.groupby(['STAFF', 'Subject', 'Batch','LAB']).size().reset_index(name='StudentCount')

            # Display the grouped data
            # print(grouped_data)
            def remove_spaces(name):
                return name.replace(" ", "")

            # Apply the function to remove spaces from the 'STAFF' column
            grouped_data['STAFF'] = grouped_data['STAFF'].apply(remove_spaces)

            # Display the updated grouped data
            # print(grouped_data)
            # Remove the index column
            grouped_data.reset_index(drop=True, inplace=True)

            # Save the DataFrame to an Excel file
            grouped_data.to_excel("staff_subject_counts.xlsx", index=False)
            
            # MongoDB connection


            # Check if the collection is empty
            if collection.count_documents({}) == 0:
                # Read the Excel file
                df = pd.read_excel("staff_subject_counts.xlsx")

                # Convert DataFrame to a list of dictionaries
                data = df.to_dict(orient='records')

                # Insert data into MongoDB
                collection.insert_many(data)

            
    return redirect("/home")



@app.route('/home')
def index():
    # Retrieve unique teacher names from MongoDB
    distinct_teacher_names = collection.distinct("STAFF")
    distinct_batch_names=collection.distinct("Batch")
    distinct_subject_names=collection.distinct("Subject")
    return render_template('home.html', teacher_names=distinct_teacher_names,batch_names=distinct_batch_names,subject_names=distinct_subject_names)

from flask import render_template

@app.route('/get_teacher_info', methods=['POST'])
def get_teacher_info():
    teacher_name = request.form['teacher_name']
    
    # Retrieve information for the selected teacher from MongoDB
    teacher_info_cursor = collection.find({'STAFF': teacher_name}, {'_id': 0, 'Batch': 1, 'Subject': 1, 'LAB': 1, 'StudentCount': 1})
    
    # Convert cursor to list of dictionaries
    teacher_info = list(teacher_info_cursor)
    
    # Calculate total student count and total number of batches
    total_student_count = sum(info['StudentCount'] for info in teacher_info)
    total_batches = len(teacher_info)
    
    # Render teacher_info.html template with teacher info
    return render_template('teacher_info.html', teacher_name=teacher_name, teacher_info=teacher_info, total_student_count=total_student_count, total_batches=total_batches)

from flask import render_template

@app.route('/get_batch_info', methods=['POST'])
def get_batch_info():
    batch_name = request.form['batch_name']
    
    # Retrieve information for the selected batch from MongoDB
    batch_info_cursor = collection.find({'Batch': batch_name}, {'_id': 0, 'STAFF': 1, 'Subject': 1, 'StudentCount': 1})
    
    # Convert cursor to list of dictionaries
    batch_info = list(batch_info_cursor)
    
    # Calculate total student count
    total_student_count = sum(info['StudentCount'] for info in batch_info)
    
    # Render batch_info.html template with batch info
    return render_template('batch_info.html', batch_name=batch_name, batch_info=batch_info, total_student_count=total_student_count)

@app.route('/get_subject_info', methods=['POST'])
def get_subject_info():
    subject_name = request.form['subject_name']
    
    # Retrieve information for the selected subject from MongoDB
    subject_info_cursor = collection.find({'Subject': subject_name}, {'_id': 0, 'STAFF': 1, 'Batch': 1, 'StudentCount': 1})
    
    # Convert cursor to list of dictionaries
    subject_info = list(subject_info_cursor)
    
    # Calculate total student count
    total_student_count = sum(info['StudentCount'] for info in subject_info)
    
    # Render subject_info.html template with subject info
    return render_template('subject_info.html', subject_name=subject_name, subject_info=subject_info, total_student_count=total_student_count)


if __name__ == '__main__':
    app.run(debug=True)

# import pandas as pd
# from pymongo import MongoClient

# # Read the Excel sheet into a DataFrame
# df = pd.read_excel("staff_subject_counts.xlsx")

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")
# db = client["your_database"]
# collection = db["your_collection"]

# # Iterate over each row in the DataFrame
# for index, row in df.iterrows():
#     # Prepare the document to insert into MongoDB
#     doc = {
#         "STAFF": row["STAFF"],
#         "Subject": row["Subject"],
#         "Batch": row["Batch"],
#         "LAB": row["LAB"],
#         "Student Count": row["Student Count"]
#     }
    
#     # Insert the document into the MongoDB collection
#     collection.insert_one(doc)

# print("Data inserted into MongoDB successfully.")

