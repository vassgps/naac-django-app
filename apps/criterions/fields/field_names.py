# Criterions/Fieldnames.py

"""
# For Char Field follow the thump rules
# Selection Menus - char1, char2, char3
# Number fields - char8
# Additional info links - url1
# Additional Info Files file1
# Main date for year - date

#Field name definitions
# fc - Field names in criteria - For show field in forms and display obj.field in HTML files
# sc - Search fields. Only for show search options in the form
# dc - Dictionry of Criterion - SHow Full Field name (Question's) Linked to field name.
       This key value pairs are used in Create and Update form data, HTML table Headers and report generation
"""

# --------------* Fields for Criteria 1.1.1 * --------------------------------
fc1_1_1 = ('date', 'batch', 'program', 'paper', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')

sc1_1_1 = ('program', 'batch', 'status',)

dc1_1_1 = {'date': 'Date', 'batch': 'Batch', 'program': 'Program', 'paper': 'Paper', 'text1': 'Learning_objective',
           'text2': 'Relevance', 'text3': 'Beneficiaries', 'text4': 'Course Outcome', 'text5': 'Program Outcome',
           'text6': 'Program Specific Outcome', 'file1': 'Additional Info Files', 'url1': 'Additional Info Links'}

# ------------------------* Fields for Criteria 1.1.2 * -------------------------------- #
fc1_1_2 = ('date', 'department', 'program',  'text2', 'text3', 'text4', 'text5', 'date2',
           'date3', 'file2', 'file3', 'file1', 'url1')

dc1_1_2 = {'date': 'Date', 'department': 'Department', 'program': 'Program', 'text1': 'Program code ',
           'text2': 'Whether revision has been carried out in the syllabus ',
           'text3': 'Year of Revision ', 'text4': 'Percentage of syllabus content added or replaced ',
           'text5': 'If 100% Revision, Name of the New course introduced ', 'date2': 'Date of BOS Meeting ',
           'date3': 'Date of Academic Council ', 'file2': 'Minutes of relevant Academic Council/BOS meeting',
           'file3': 'Details of program syllabus revision in last 5 years(Data Template)',
           'file1': 'Additional Info Files ', 'url1': 'Additional Info Links'}

sc1_1_2 = ('department', 'program', 'status',)

# ------------------------------------------- * 1.1.3 *-------------------------------------------------------#


fc1_1_3 = ('date', 'department','program', 'paper', 'text2',  'text3', 'text4', 'text5',
           'text6', 'date2', 'date3', 'text7', 'file2', 'file3', 'file4',
           'file5', 'file1', 'url1')

dc1_1_3 = {'date': 'Date', 'department': ' Department', 'paper': 'Name of the Course ', 'text1': 'Course Code ',
           'text2': 'Type of course ', 'program': ' Program',
           'text3': 'Focus of the activity ', 'text4': 'Year of Introduction ', 'text5': 'Beneficiaries ',
           'date2': 'Date of BOS Meeting ', 'date3': 'Date of Academic Council ', 'text6': 'MOU with Organizations ',
           'text7': 'Impact / Outcome ',
           'file2': 'Programme / Curriculum/ Syllabus of the courses',
           'file3': ' Minutes of the Boards of Studies/ Academic Council meetings with approvals for these courses',
           'file4': 'MoUs with relevant organizations for these courses, if any',
           'file5': 'Average percentage of courses having focus on employability/ entrepreneurship(Data Template)',
           'file1': ' Additional Info files',
           'url1': 'Additional info Links'}

sc1_1_3 = ('department', 'program', 'paper', 'status')

# ------------------------------------------- * 1.2.1 *-------------------------------------------------------#
fc1_2_1 = ('date', 'department','program',  'paper',  'text2', 'date2', 'date3',
           'file1', 'url1')

dc1_2_1 = {'date': 'Date', 'department': ' Department', 'paper': 'Course ', 'text1': 'Course code ',
           'program': 'Name of the Program', 'text2': 'Year of Introduction ', 'date2': 'Date of BOS meeting ',
           'date3': 'Date of Academic Council meeting ',
           'file1': ' Additional Info files', 'url1': 'Additional info Links'}

sc1_2_1 = ('department', 'program', 'paper', 'status')

# ------------------------------------------- * 1.2.2 *-------------------------------------------------------#

fc1_2_2 = ('date', 'program',  'text2', 'text3', 'text4', 'date2', 'date3',
           'file1', 'url1')

dc1_2_2 = {'date': 'Date', 'program': ' Program', 'text2': 'CBSE or Elective ',
           'text1': 'Program Code ', 'text3': 'Name of program adopting',
           'text4': 'Year of Implementation', 'date2': 'Date of BOS Meeting ', 'date3': 'Date of Academic Council',
           'file1': ' Additional Info files', 'url1': 'Additional info Links'}

sc1_2_2 = ('program', 'status')

# ------------------------------------------- * 1.3.1 *-------------------------------------------------------#

fc1_3_1 = ('date', 'department', 'program', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6',
           'text7', 'text8', 'file1', 'url1')

dc1_3_1 = {'date': 'Date', 'department': ' Department', 'program': 'name of the Program',
           'text1': 'Name of the course dealing in Cross cutting issues ', 'text2': 'Cross cutting issues',
           'text3': 'Activities ', 'text4': 'External or Internal Resource persons ',
           'text5': 'Number of Beneficiaries ', 'text6': 'Issues Addressed ', 'text7': 'Outcome',
           'text8': 'Committee in charge',
           'file1': ' Additional Info files', 'url1': 'Additional info Links'}

sc1_3_1 = ('department', 'program', 'status')

# ------------------------------------------- * 1.3.2 *-------------------------------------------------------#

fc1_3_2 = ('date', 'department', 'text1', 'text2', 'text3', 'text5', 'text6', 'text7', 'text8',
           'text9', 'text10', 'text11', 'text12', 'text13', 'date2', 'date3', 'date4',
           'text14', 'file2', 'file3', 'file1', 'url1')

dc1_3_2 = {'date': 'Date', 'department': ' Department', 'text1': 'Value Added Course Introduced ',
           'text2': 'Course code ', 'text3': 'Year of Implementation ', 'text5': 'Number of Contact Hours',
           'text6': 'Faculty Incharge ', 'text7': 'Activities ', 'text8': 'Agency with Contact details ',
           'text9': 'External resource person ', 'text10': 'Number of Students Registration ',
           'text11': 'Number of students completed the course ', 'text12': 'Number of times the course offered /year ',
           'text13': 'Year of Discontinuation ', 'date2': 'Date of BOS Meeting ', 'date3': 'Date of Governing Body',
           'date4': 'Date of Academic Council ', 'text14': 'Outcome',
           'file2': 'Brochure or any other document relating to value added courses',
           'file3': 'List of value added courses (Data Template)',
           'file1': 'Additional Info files', 'url1': 'Additional info Links'}

sc1_3_2 = ('department', 'status')

# ------------------------------------------- * 1.3.3 *-------------------------------------------------------#

fc1_3_3 = ('date', 'department', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7',
           'text8', 'text9', 'text10', 'text11', 'text12', 'file2', 'file1', 'url1')

dc1_3_3 = {'date': 'Date', 'department': ' Department', 'text1': 'Value Added Course introduced',
           'text2': 'Year of Implementation', 'text3': 'Course code', 'text4': 'Number of Contact Hours',
           'text5': 'Faculty Charge', 'text6': 'Activities', 'text7': 'External Resource Person',
           'text8': 'Number of Students Registration', 'text9': 'Number of students Completed the course',
           'text10': 'Number of times Course Offered per year ', 'text11': 'Year of Discontinuation of the Course',
           'text12': 'Outcome', 'file2': 'List of students enrolled',
           'file1': ' Additional Info files', 'url1': 'Additional info Links'}

sc1_3_3 = ('department', 'status')

# ------------------------------------------- * 1.3.4 *-------------------------------------------------------#

fc1_3_4 = ('date', 'department', 'program', 'text2', 'text3', 'text4', 'text5',
           'text6', 'text7', 'text8', 'file2', 'file1', 'url1')

dc1_3_4 = {'date': 'Date', 'department': ' Department', 'program': ' Program name', 'text1': 'Program Code',
           'text2': 'Tutor in Charge',
           'text3': 'Number of students undertaking field project ', 'text4': 'Areas of Field Project',
           'text5': 'Areas of Internships', 'text6': 'Number of Students Undertaking Internship ',
           'text7': 'Institution of Internship ', 'text8': 'Duration Of Internship ',
           'file2': ' Data Template(List of Programs & No. of students) ',
           'file1': ' Additional Info files',
           'url1': 'Additional info Links'}

sc1_3_4 = ('department', 'program', 'status')

# ------------------------------------------- * 1.4.1 *-------------------------------------------------------#


fc1_4_1 = ('date', 'department', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7',
           'date2', 'file1', 'url1')

dc1_4_1 = {'date': 'Date', 'department': ' Department', 'text1': 'Semester ', 'text2': 'Student feed back',
           'text3': 'Teacher Feed back', 'text4': 'Employee feed back ', 'text5': 'Alumni feed back ',
           'text6': 'Parents Feed back ', 'text7': 'Action Taken ', 'date2': 'Minutes Date ',
           'file1': ' Additional Info files', 'url1': 'Additional info Links'}

sc1_4_1 = ('department', 'status')

# ------------------------------------------- * 1.4.2 *-------------------------------------------------------#

fc1_4_2 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'date2', 'date3', 'date4',
           'text7', 'file1', 'url1')

dc1_4_2 = {'date': 'Date', 'text1': 'Type of feed Back ', 'text2': 'Year ', 'text3': 'Collected or Not Collected',
           'text4': 'Analysed or Not AAnalysed ', 'text5': 'Action Taken or Not ',
           'text6': 'Published / Not published in website ', 'date2': 'Date of Governing Council meeting ',
           'date3': 'Date of Academic Council Meeting', 'date4': ' Date of Board of Management meeting',
           'text7': 'Involvement of Stake Holders ', 'file1': ' Additional Info files', 'url1': 'Additional info Links'}

sc1_4_2 = ('status',)

# ------------------------------------------- * 2.1.1 *------------------------------------- OK

fc2_1_1 = ('date', 'program', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')

dc2_1_1 = {'date': 'Year of Enrollment', 'program': 'Programme Joined',
           'text2': 'Name of Students from other states', 'text3': 'Contact Details of The Students',
           'text4': 'Name of Students from other countries', 'text5': 'Contact Details of The Students',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_1_1 = ('program', 'status')

# --------------------------* 2.1.2 *--------------------------------------- Ok
fc2_1_2 = ('date', 'program', 'text4', 'text5', 'text6', 'file1', 'url1')
dc2_1_2 = {'date': 'Year of admission', 'program': 'Program Name', 'text1': 'Program Code',
           'text4': 'No. of Seats available', 'text5': 'No. of Eligible applications received',
           'text6': 'No. of students admitted',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_1_2 = ('program', 'status')

# --------------------------* 2.1.3 *---------------------------------------
fc2_1_3 = ('date', 'file1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc2_1_3 = {'date': 'Year of admission', 'text2': 'Reserved seats(Aided)', 'text3': 'Admitted seats(Aided)',
           'text4': 'Reserved seats for Un-Aided', 'text5': 'Admitted seats for Un-Aided',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_1_3 = ('status',)

# --------------------------* 2.2.1 *--------------------------------------- OK
fc2_2_1 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10',
           'text11', 'text12', 'file1', 'url1')
dc2_2_1 = {'date': 'Year', 'department': 'Department', 'text2': 'Class', 'text3': 'Methods of assessment',
           'text4': 'Special programs for advanced learners', 'text5': 'Resource Person',
           'text6': 'No. of Beneficiaries ', 'text8': 'Outcome', 'text9': 'Special programs for slow learners ',
           'text10': 'Resource Person', 'text11': 'No. of Beneficiaries ', 'text12': 'Outcome',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_2_1 = ('department', 'status',)
# --------------------------* 2.2.2 *--------------------------------------- OK
fc2_2_2 = ('date', 'department', 'program', 'text4', 'text5', 'text6', 'file1', 'url1')
dc2_2_2 = {'date': 'Year', 'department': 'Department', 'program': 'Name of the Program',
           'text4': 'Total No.of Students Enrolled', 'text5': 'No. of Full time teachers',
           'text6': 'No. of Guest Teachers',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_2_2 = ('department', 'program', 'status')

# --------------------------* 2.2.3 *---------------------------------------ok


fc2_2_3 = ('date', 'department', 'program', 'text4', 'text5', 'file1', 'url1')

dc2_2_3 = {'date': 'Year', 'department': 'Department', 'program': 'Program',
           'text4': 'Name of the student enrolled', 'text5': 'Gender',
           'text6': 'Unique disability ID Card No', 'text7': 'Type of disability',
           'text8': 'Percetage of disability ',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}

sc2_2_3 = ('department', 'program', 'status')

# --------------------------* 2.3.1 *--------------------------------------- ok
fc2_3_1 = ('date', 'department', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9',
           'file2', 'file1', 'url1')
dc2_3_1 = {'date': 'Year', 'department': 'Department', 'text1': 'Faculty', 'text2': 'Designation',
           'text3': 'Experiential Learning', 'text4': 'Participative Learning', 'text5': 'Problem-Solving Methodology',
           'text6': 'Seminars', 'text8': 'Any Other', 'text9': 'Outcome ', 'file2': 'Document',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}

sc2_3_1 = ('status',)

# --------------------------* 2.3.2 *--------------------------------------- ok
fc2_3_2 = ('date', 'department', 'text3', 'text4', 'text5', 'file1', 'url1')
dc2_3_2 = {'date': 'Year ', 'department': 'Department', 'text3': 'Name of Faculty',
           'text4': 'Whether Using ICT or NOT', 'text5': 'ICT tools used (LMS / E-resources)',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_3_2 = ('department', 'status',)
# --------------------------* 2.3.3 *--------------------------------------- ok
fc2_3_3 = ('date', 'department', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10',
           'file2', 'file1', 'url1')
dc2_3_3 = {'date': 'Year', 'department': 'Department', 'text3': 'Class', 'text4': 'Name of the Mentors ',
           'text5': 'No. of Students assigned to each mentor', 'text6': 'Academic issues addressed',
           'text8': 'Stress related issues addressed', 'text9': 'Solution for academic issues',
           'text10': 'Solution for stress issues', 'file2': 'Document',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_3_3 = ('department', 'status',)

# --------------------------* 2.3.4 *---------------------------------------ok
fc2_3_4 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file2', 'file1', 'url1')
dc2_3_4 = {'date': 'Year', 'department': 'Department', 'text2': 'Semester', 'text3': 'Faculty',
           'text4': 'Papers',
           'text5': 'Preparation of Teaching plan', 'text6': '% of Execution as per the teaching plan',
           'text8': 'Adherence to academic calender', 'file2': 'Document ', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc2_3_4 = ('status',)
# --------------------------* 2.4.1 *--------------------------------------- ok
fc2_4_1 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc2_4_1 = {'date': 'Year', 'department': 'Department', 'text2': 'Name of the full time teacher',
           'text3': 'PAN Number',
           'text4': 'Designation', 'text5': 'No. of Sanctioned Posts', 'text6': 'Year of Appointment',
           'text8': 'Total Years of Experience ',
           'text9': 'Is the teacher still serving the institution / if not last year of the service of faculty to the institution',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_4_1 = ('department', 'status',)

# --------------------------* 2.4.2 *--------------------------------------- ok
fc2_4_2 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc2_4_2 = {'date': 'Year ', 'department': 'Department', 'text2': 'Name of the full time teacher with Ph.D',
           'text3': 'Year of obtaining Ph.D', 'text4': 'Whether recognized as research guide',
           'text5': 'Year of recognition as research Guide', 'text6': 'No of Research Scholars enrolled ',
           'text8': 'No. of Ph.D Awarded', 'text9': 'Remarks', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc2_4_2 = ('department', 'status',)
# --------------------------* 2.4.3 *---------------------------------------
fc2_4_3 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc2_4_3 = {'date': 'Year', 'department': 'Department', 'text2': 'Name of the Faculty',
           'text3': 'Designation',
           'text4': 'Full time / Guest ', 'text5': 'Years of experience', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc2_4_3 = ('department', 'status',)

# --------------------------* 2.4.4 *--------------------------------------- ok
fc2_4_4 = (
    'date', 'department', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file2', 'file1', 'url1')
dc2_4_4 = {'date': 'Year', 'department': 'Department', 'text1': 'Faculty', 'text2': 'Designation', 'text3': 'Year ',
           'text4': 'Awards / recognition', 'text5': 'Government / Non Government',
           'text6': 'International / National / State / Local Bodies', 'text8': 'Incentives', 'file2': 'Document',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_4_4 = ('department', 'status',)

# --------------------------* 2.4.5 *---------------------------------------ok
fc2_4_5 = ('date', 'department', 'text2', 'text3', 'text4', 'file1', 'url1')
dc2_4_5 = {'date': 'Year', 'department': 'Department',
           'text2': 'Name of the Full time teachers from other states',
           'text3': 'Domicile Status ', 'text4': 'State from which qualifying degree was obtained',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_4_5 = ('status',)
# --------------------------* 2.5.1 *--------------------------------------- ok
fc2_5_1 = ('date', 'program', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc2_5_1 = {'date': 'Year ', 'program': 'Program Name', 'text1': 'Program Code', 'text3': 'Semester ',
           'text4': 'Date of Commencement of end semester exam', 'text5': 'End date of exam',
           'text6': 'Date of declaration  of results', 'text8': 'No. of days taken for declaration of result',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_5_1 = ('program', 'status',)

# --------------------------* 2.5.2 *--------------------------------------- OK
fc2_5_2 = ('date', 'department', 'program', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc2_5_2 = {'date': 'Year', 'department': 'Department', 'program': 'Program', 'text3': 'Semester',
           'text4': 'Complaints Registered', 'text5': 'Nature of complaint', 'text6': 'Grievances addressed',
           'text8': 'Time taken to redressed the issue', 'text9': 'Outcome', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc2_5_2 = ('department', 'program', 'status',)
# --------------------------* 2.5.3 *---------------------------------------
fc2_5_3 = ('date', 'text1', 'program', 'paper', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc2_5_3 = {'date': 'Year ', 'text1': 'Semester', 'program': 'Program', 'paper': 'Paper',
           'text4': 'No. of students appeared for exam', 'text5': 'No. of applications for revaluation',
           'text6': 'No. of revaluation case where marks changed', 'text8': 'Time taken to publish revaluation result',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_5_3 = ('program', 'paper', 'status',)
# --------------------------* 2.5.4 *--------------------------------------- OK
fc2_5_4 = ('date', 'text1', 'program', 'paper', 'date2', 'text5', 'file1', 'url1')
dc2_5_4 = {'date': 'Year', 'text1': 'Semester', 'program': 'Program', 'paper': 'Papers',
           'date2': 'Date of Uploading Internal Assessment', 'text5': 'Exam Procedure',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_5_4 = ('program', 'paper', 'status',)

# --------------------------* 2.5.5 *--------------------------------------- OK
fc2_5_5 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc2_5_5 = {'date': 'Year', 'text1': 'Percentage of automation', 'text2': 'Implementation of EMS',
           'text3': 'Method of Student Registration ', 'text4': 'Method of Issuing Hall Ticket',
           'text5': 'Method of processing Result', 'text6': 'Method of publishing Result',
           'text8': 'Manual of Examination', 'text9': 'Report of Examination',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_5_5 = ('status',)

# --------------------------* 2.6.1 *--------------------------------------- OK
fc2_6_1 = ('date', 'program', 'text1', 'text4', 'text5', 'text6', 'text7', 'text8', 'file1', 'url1')
dc2_6_1 = {'date': 'Year', 'text1': 'Semester ', 'program': 'Program ', 'text1': 'Program code',
           'text4': 'Program outcome', 'text5': 'Program specific outcome', 'text6': 'Course outcome',
           'text7': 'Method Communication to teachers ',
           'text8': 'Method Communication to Students', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc2_6_1 = ('program', 'status',)
# --------------------------* 2.6.2 *--------------------------------------- OK
fc2_6_2 = ('date', 'text1', 'program', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10', 'file1',
           'url1')
dc2_6_2 = {'date': 'Year ', 'text1': 'Semester', 'program': 'Program', 'text3': 'Course',
           'text4': 'Program Outcome', 'text5': 'Program Outcome evaluation  ', 'text6': 'Program Specific Outcome ',
           'text8': 'Program Specific Outcome evaluation', 'text9': 'Course Outcome',
           'text10': 'Course Outcome evaluation',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_6_2 = ('program', 'status',)
# --------------------------* 2.6.3 *--------------------------------------- OK
fc2_6_3 = ('date', 'text3', 'program', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10', 'text11',
           'text12', 'file1', 'url1')
dc2_6_3 = {'date': 'Year ', 'text3': 'Semester', 'program': 'Program Name', 'text1': 'Program Code',
           'text4': 'No. of Students appeared in the final year examination', 'text5': 'No. of Students Passed',
           'text6': 'Pass Percentage', 'text8': 'Above 90%', 'text9': '80% -90%', 'text10': '70% - 80%',
           'text11': '60% - 70%',
           'text12': '50% - 60 %', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc2_6_3 = ('program', 'status',)
# --------------------------* 2.7.1 *--------------------------------------- OK
fc2_7_1 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'program', 'text10', 'text11',
           'text12', 'text13', 'file1', 'url1')

dc2_7_1 = {'date': 'Year', 'text1': 'Semester', 'text2': 'Name of the student', 'text3': 'Gender',
           'text4': 'category', 'text5': 'state of domicile', 'text6': 'nationality', 'text8': 'e-mail id',
           'program': 'Program Name ', 'text10': 'Student unique enrollment id', 'text11': 'Mobile no',
           'text12': 'Aadhar no', 'text13': 'Year of joining', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc2_7_1 = ('program', 'status',)

# --------------------------* 3.1.1 *--------------------------------------- OK
fc3_1_1 = ('date', 'text1', 'date2', 'date3', 'date4', 'file1', 'url1')
dc3_1_1 = {'date': 'Year', 'text1': 'Policy for Promotion Research', 'date2': 'Dates of minutes of governing council',
           'date3': 'Dates of minutes Board of Management', 'date4': 'Dates of minutes academic council',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_1_1 = ('status',)

# --------------------------* 3.1.2 *--------------------------------------- OK
fc3_1_2 = ('date', 'text1', 'text2', 'text3', 'date2', 'text5', 'file1', 'url1')
dc3_1_2 = {'date': 'Year', 'text1': 'Name of the faculty receiving seed money',
           'text2': 'Amount of Seed Money', 'text3': 'Duration of the grant',
           'date2': 'Date of minutes of relevant body',
           'text5': 'Type of Research', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_1_2 = ('status',)
# --------------------------* 3.1.3 *--------------------------------------- OK
fc3_1_3 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc3_1_3 = {'date': 'Year', 'department': 'Department', 'text2': 'Faculty ', 'text3': 'Designation ',
           'text4': 'Name of the award', 'text5': 'Awarding Agency', 'text6': 'Document No',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_1_3 = ('status',)

# --------------------------* 3.1.4 *--------------------------------------- OK
fc3_1_4 = ('date', 'file1', 'url1')
dc3_1_4 = {'date': 'Year', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_1_4 = ('status',)

# --------------------------* 3.2.1 *--------------------------------------- OK
fc3_2_1 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10',
           'text11', 'file1', 'url1')
dc3_2_1 = {'date': 'Year', 'department': 'Department', 'text2': 'Faculty ', 'text3': 'Designation ',
           'text4': 'Year of award', 'text5': 'Minor/Major', 'text6': 'Duration', 'text8': 'Fund',
           'text9': 'Government / Non Government', 'text10': 'Status', 'text11': 'Documents',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_2_1 = ('status',)
# --------------------------* 3.2.2 *--------------------------------------- OK
fc3_2_2 = ('date', 'file1', 'url1')
dc3_2_2 = {'date': 'Year', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_2_2 = ('status',)

# --------------------------* 3.2.3 *--------------------------------------- OK
fc3_2_3 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc3_2_3 = {'date': 'Year', 'department': 'Department', 'text2': 'Name of the Faculty', 'text3': 'Designation',
           'text4': 'Year of Recognition ', 'text5': 'No. of Students Enrolled', 'text6': 'No. of Students Awarded',
           'text8': 'Documents', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_2_3 = ('status',)
# --------------------------* 3.2.4 *--------------------------------------- OK
fc3_2_4 = ('date', 'file1', 'url1')
dc3_2_4 = {'date': 'Year', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_2_4 = ('status',)

# --------------------------* 3.3.1 *--------------------------------------- OK
fc3_3_1 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc3_3_1 = {'date': 'Year', 'department': 'Department', 'text2': 'Incubation Centre', 'text3': 'Name',
           'text4': 'Sponsoring Agent', 'text5': 'Name of the Startup', 'text6': 'Nature of Startup',
           'text8': 'Date of Commencement', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_3_1 = ('status',)

# --------------------------* 3.3.2 *--------------------------------------- OK
fc3_3_2 = (
    'date', 'department', 'date2', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10', 'text11',
    'file1', 'url1')
dc3_3_2 = {'date': 'Year', 'date2': 'Date & Year', 'department': 'Department', 'text2': 'Incubation Centre',
           'text3': 'IPR / Industry-Academia Innovative practices /Others', 'text4': 'Workshop / Seminar',
           'text5': 'Type of Seminar (National/International/Regional)', 'text6': 'Title', 'text8': 'Resource Person',
           'text9': 'Beneficiaries ', 'text10': 'Document No', 'text11': 'Others',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_3_2 = ('status',)
# --------------------------* 3.3.3 *--------------------------------------- OK
fc3_3_3 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc3_3_3 = {'date': 'Year', 'department': 'Department', 'text2': 'Name of awardee', 'text3': 'Designation',
           'text4': 'Year', 'text5': 'Awarding Agency', 'text6': 'Title of the innovation', 'text8': 'Date of Award',
           'text9': 'Document', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_3_3 = ('status',)

# --------------------------* 3.4.1 *--------------------------------------- OK
fc3_4_1 = ('date', 'file1', 'url1')
dc3_4_1 = {'date': 'Year', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_4_1 = ('status',)

# --------------------------* 3.4.2 *--------------------------------------- OK
fc3_4_2 = ('date', 'file1', 'url1')
dc3_4_2 = {'date': 'Year', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_4_2 = ('status',)

# --------------------------* 3.4.3 *--------------------------------------- OK
fc3_4_3 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc3_4_3 = {'date': 'Year', 'department': 'Department', 'text2': 'Name ', 'text3': 'Designation ',
           'text4': 'Year of submission', 'text5': 'Year of awarding', 'text6': 'Patent Number',
           'text8': 'Title of the Patent', 'text9': 'Document', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc3_4_3 = ('status',)
# --------------------------* 3.4.4 *--------------------------------------- OK
fc3_4_4 = ('date', 'text1', 'department', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc3_4_4 = {'date': 'Year', 'text1': 'Name of the PhD scholar', 'department': 'Name of the Department',
           'text3': 'Name of the guide/s', 'text4': 'Title of the thesis',
           'text5': 'Year of registration of the scholar', 'text6': 'Year of award of PhD',
           'text8': 'Name of the supporting documents attached*',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_4_4 = ('status',)

# --------------------------* 3.4.5 *--------------------------------------- OK
fc3_4_5 = (
    'date', 'text1', 'text2', 'department', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10', 'text11', 'text12',
    'text13', 'file2', 'file1', 'url1')
dc3_4_5 = {'date': 'Year', 'text1': 'Title of paper', 'text2': 'Name of the author/s',
           'department': 'Department of the teacher', 'text4': 'Designation ', 'text5': 'Name of journal',
           'text6': 'National/International', 'text8': 'Year of publication', 'text9': 'Average Impact Factor, if any',
           'text10': 'ISS0 Number', 'text11': 'UGC listed or not',
           'text12': 'Name of the supporting documents attached*',
           'text13': 'Journal Link ', 'file2': 'Document', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc3_4_5 = ('status',)
# --------------------------* 3.4.6 *--------------------------------------- OK
fc3_4_6 = (
    'date', 'text1', 'department', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10', 'text11', 'text12',
    'text13', 'text14', 'file1', 'url1')
dc3_4_6 = {'date': 'Year', 'text1': 'Name of the faculty ', 'department': 'Department',
           'text3': 'Book/Chapter/Conference Proceedings', 'text4': 'Title of the book/chapters published',
           'text5': 'Title of the paper', 'text6': 'Title of the proceedings of the conference',
           'text8': 'Name of the conference', 'text9': 'National / international', 'text10': 'Year of publication',
           'text11': 'ISBN/ISSN  number of the proceeding',
           'text12': 'Affiliating Institute at the time of publication',
           'text13': 'Name of the publisher', 'text14': 'Name of the supporting documents attached*',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_4_6 = ('status',)
# --------------------------* 3.4.7 *---------------------------------------
fc3_4_7 = ('date', 'text1', 'department', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10',
           'text11', 'file1', 'url1')
dc3_4_7 = {'date': 'Year', 'text1': 'Name of the Author', 'department': 'Department', 'text3': 'Designation',
           'text4': 'Title of the paper', 'text5': 'Title of the journal', 'text6': 'year of publication',
           'text8': 'Citation index', 'text9': 'Institutional affiliation as mentioned in the publication ',
           'text10': 'No. of citation excluding self citation ', 'text11': 'INFLIBNET Data',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_4_7 = ('status',)
# --------------------------* 3.4.8 *--------------------------------------- ) OK
fc3_4_8 = ('date', 'text1', 'department', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10',
           'text11', 'file1', 'url1')
dc3_4_8 = {'date': 'Year', 'text1': 'Name of the Author', 'department': 'Department', 'text3': 'Designation',
           'text4': 'Title of the paper', 'text5': 'Title of the journal', 'text6': 'year of publication',
           'text8': 'H-Index', 'text9': 'Institutional affiliation as mentioned in the publication',
           'text10': 'No. of citation excluding self citation ', 'text11': 'INFLIBNET Data',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_4_8 = ('department', 'status',)
# --------------------------* 3.5.1 *---------------------------------------OK
fc3_5_1 = ('date', 'text1', 'department', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc3_5_1 = {'date': 'Year', 'text1': 'Faculty', 'department': 'Department',
           'text3': 'Name of the consultancy project', 'text4': 'consulting / sponsoring agency with contact details',
           'text5': 'Revenue Generated in Rs', 'text6': 'Consultancy Policy (Yes /No)',
           'text8': 'Audited Statement (Yes /No) ', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc3_5_1 = ('department', 'status',)

# --------------------------* 3.5.2 *---------------------------------------OK
fc3_5_2 = ('date', 'file1', 'url1')
dc3_5_2 = {'date': 'Year', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_5_2 = ('status',)
# --------------------------* 3.5.3 *--------------------------------------- Ok
fc3_5_3 = ('date', 'text1', 'text2', 'department', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc3_5_3 = {'date': 'Year', 'text1': 'Name of the teacher - Consultants', 'text2': 'Designation ',
           'department': 'Department ', 'text4': 'Title of the corporate training program',
           'text5': 'Agency seeking training with contact details ', 'text6': 'Revenue generated in RS.',
           'text8': 'No. of Trainees / Beneficiaries ', 'text9': 'Audited Statement (Yes /No) ',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_5_3 = ('department', 'status',)
# --------------------------* 3.6.1 *--------------------------------------- OK
fc3_6_1 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9',
           'text10', 'text11', 'text12', 'file1', 'url1')
dc3_6_1 = {'date': 'Year', 'department': 'Department', 'text2': 'Faculty In-charge ', 'text3': 'Social Issue',
           'text4': 'Activity (To Tackle Social Issue)', 'text5': 'Date of activity/Duration',
           'text6': 'Area of operation',
           'text8': 'No. of participants ', 'text9': 'No of beneficiaries', 'text10': 'Method of operation',
           'text11': 'Resource Person ', 'text12': 'Impact', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc3_6_1 = ('department', 'status',)
# --------------------------* 3.6.2 *--------------------------------------- OK


fc3_6_2 = ('date', 'text1', 'department', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc3_6_2 = {'date': 'Year', 'text1': 'Activity ', 'department': 'Department / Club', 'text3': 'Teacher in-charge',
           'text4': 'Awards / Recognition', 'text5': 'A brief note of the award',
           'text6': 'Name of the awarding agency / Government', 'text8': 'Regional/State/National/International',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_6_2 = ('department', 'status',)
# --------------------------* 3.6.3 *--------------------------------------- OK
fc3_6_3 = ('date', 'date2', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc3_6_3 = {'date': 'Year', 'date2': 'Date', 'text1': 'Activity ',
           'text2': 'Organising unit or agency (Department / Club)',
           'text3': 'Collaborating Agency with contact detail', 'text4': 'No. of Participants',
           'text5': 'Area of operation', 'text6': 'No. of Beneficiaries ', 'text8': 'Result',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_6_3 = ('status',)
# --------------------------* 3.6.4 *--------------------------------------- OK
fc3_6_4 = ('date', 'date2', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8',
           'text9', 'file1', 'url1')
dc3_6_4 = {'date': 'Year', 'date2': 'Date', 'department': 'Department / Clubs', 'text2': 'Activity',
           'text3': 'Collaborating agency if any', 'text4': 'Name of the scheme', 'text5': 'No of participants ',
           'text6': 'area of operation ', 'text8': 'No of beneficiaries ', 'text9': 'Impact',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_6_4 = ('department', 'status',)
# --------------------------* 3.7.1 *--------------------------------------- OK
fc3_7_1 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10',
           'text11', 'file1', 'url1')
dc3_7_1 = {'date': 'Year', 'department': 'Department', 'text2': 'Faculty In-charge',
           'text3': 'Title of the collaborative activity ', 'text4': 'Collaborating agency with contact detail',
           'text5': 'name of the participants ', 'text6': 'Source of financial Support', 'text8': 'Amount',
           'text9': 'Nature of Activity', 'text10': 'Duration from', 'text11': 'Duration To',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_7_1 = ('department', 'status',)
# --------------------------* 3.7.2 *--------------------------------------- OK
fc3_7_2 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10',
           'text11', 'file1', 'url1')
dc3_7_2 = {'date': 'Year', 'department': 'Department', 'text2': 'Title of the linkage ',
           'text3': 'Name of the institution linked with contact detail', 'text4': 'nature of contract ',
           'text5': 'Duration from', 'text6': 'Duration to ', 'text8': 'Name of the participant',
           'text9': 'Linkage related document', 'text10': 'Place of work', 'text11': 'Nature of work',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_7_2 = ('department', 'status',)
# --------------------------* 3.7.3 *--------------------------------------- OK
fc3_7_3 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10', 'text11',
           'text12', 'file1', 'url1')
dc3_7_3 = {'date': 'Year', 'department': 'Department', 'text2': 'Faculty In-Charge',
           'text3': 'Organisation with MoU is signed(institution/industry/universities etc)',
           'text4': 'Name of the institution / Industry / Corporate houses',
           'text5': 'Status of the institution ( nation / international importance / other institution / industries/ '
                    'corporate houses)',
           'text6': 'Year of Signing MoU', 'text8': 'Duration from', 'text9': 'Duration To',
           'text10': 'List of actual activities ', 'text11': 'No. of Students / Teachers Participated',
           'text12': 'E Copy of MoU (Yes/No) ', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc3_7_3 = ('department', 'status',)
# --------------------------* 4.1.1 *--------------------------------------- OK
fc4_1_1 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10', 'text11', 'text12',
           'text13', 'text14', 'file1', 'url1')
dc4_1_1 = {'date': 'Year', 'text1': 'Department / General / Library', 'text2': 'No. of Class Rooms',
           'text3': 'No. of Laboratories', 'text4': 'List of Equipment in the labs', 'text5': 'Cost of Equipments',
           'text6': 'Source of Fund', 'text8': 'Software', 'text9': 'Smart Classroom', 'text10': 'Classroom with LCD',
           'text11': 'No. of Computers', 'text12': 'E-learning resources', 'text13': 'Others',
           'text14': 'Department Library',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_1_1 = ('status',)
# --------------------------* 4.1.2 A *--------------------------------------- OK
fc4_1_2A = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc4_1_2A = {'date': 'Year', 'text1': 'Sports Infrastructure', 'text2': 'Year of Establishment',
            'text3': 'Area ', 'text4': 'Facilities', 'text5': 'No. of Users ', 'text6': 'Sports Events',
            'text8': 'Coaching arranged', 'text9': 'Additional Information', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc4_1_2A = ('status',)
# --------------------------* 4.1.2 b *--------------------------------------- OK
fc4_1_2B = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc4_1_2B = {'date': 'Year', 'text1': 'Equipments', 'text2': 'No. of Equipments', 'text3': 'No. of Users ',
            'text4': 'Additional Information', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_1_2B = ('status',)
# --------------------------* 4.1.2  C *--------------------------------------- OK
fc4_1_2C = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc4_1_2C = {'date': 'Year', 'text1': 'Events', 'text2': 'No. of players', 'text3': 'Coaching provided',
            'text4': 'Achievements (Position) ', 'text5': 'Name / Names of the student/s',
            'text6': 'Level (University / State / National / International) ', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc4_1_2C = ('status',)
# --------------------------* 4.1.2 D *--------------------------------------- OK
fc4_1_2D = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc4_1_2D = {'date': 'Year', 'text1': 'Infrastructure', 'text2': 'Facilities', 'text3': 'No. of Users',
            'text4': 'Additional Information', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_1_2D = ('status',)
# --------------------------* 4.1.2 E *--------------------------------------- OK
fc4_1_2E = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc4_1_2E = {'date': 'Year', 'text1': 'Event', 'text2': 'College / Department / Club ',
            'text3': 'Coaching Provided', 'text4': 'Achievements (Position)',
            'text5': 'Level (B-Zone / Inter Zone / South Zone)', 'text6': 'Names of outstanding performers',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_1_2E = ('status',)
# --------------------------* 4.1.3 *--------------------------------------- OK
fc4_1_3 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc4_1_3 = {'date': 'Year', 'text1': 'Name of Class room / Hall', 'text2': 'Room No / Hall Name',
           'text3': 'LCD Projector', 'text4': 'Smart ClassRoom', 'text5': 'WIFI / LAN', 'text6': 'LMS',
           'text8': 'Other ICT (Mention)', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_1_3 = ('status',)
# --------------------------* 4.1.4 *--------------------------------------- OK
fc4_1_4 = ('date', 'text1', 'text2', 'file1', 'url1')
dc4_1_4 = {'date': 'Year', 'text1': 'Item', 'text2': 'Budget Allocation in Lakhs',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_1_4 = ('status',)
# --------------------------* 4.2.1 *--------------------------------------- OK
fc4_2_1 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc4_2_1 = {'date': 'Year', 'text1': 'Name of Software',
           'text2': 'Nature of Automation (Fully or Partially) ', 'text3': 'Version', 'text4': 'Year of Automation ',
           'text5': 'Additional Information', 'text6': 'Document No ', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc4_2_1 = ('status',)
# --------------------------* 4.2.2 *--------------------------------------- OK
fc4_2_2 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc4_2_2 = {'date': 'Year', 'text1': 'Title', 'text2': 'Type (Book / Manuscript / Special Reports)',
           'text3': 'Publisher', 'text4': 'ISBN No', 'text5': 'Author', 'text6': 'No. of Copies',
           'text8': 'Year of publishing', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_2_2 = ('status',)
# --------------------------* 4.2.3 *--------------------------------------- OK
fc4_2_3 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc4_2_3 = {'date': 'Year', 'text1': 'Name of Journal', 'text2': 'YES/NO', 'text3': 'Membership Details',
           'text4': 'Subscription details', 'text5': 'Additional Information', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc4_2_3 = ('status',)
# --------------------------* 4.2.4 *--------------------------------------- OK
fc4_2_4 = ('date', 'text1', 'text2', 'text3', 'file1', 'url1')
dc4_2_4 = {'date': 'Year', 'text1': 'Rs. (in lakhs) for books Purchase ',
           'text2': 'Rs. (in lakhs) for Journals Purchase',
           'text3': 'Expenditure on subscription to E-journals and other E-resources)',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_2_4 = ('status',)
# --------------------------* 4.2.5 *--------------------------------------- OK
fc4_2_5 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc4_2_5 = {'date': 'Year', 'text1': 'Name of E-resource ', 'text2': 'Full text / Partial access',
           'text3': 'Details of Membership', 'text4': 'Details of Subscription ', 'text5': 'Validity period',
           'text6': 'Usage report from the service provider', 'text8': 'Whether remote access provided ',
           'text9': 'Web link of remote access', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc4_2_5 = ('status',)
# --------------------------* 4.2.6 *--------------------------------------- OK
fc4_2_6 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc4_2_6 = {'date': 'Year', 'text1': 'No. of teachers using library per day',
           'text2': 'No. of students using library per day', 'text3': 'No. of users using library through E-access',
           'text4': 'Method of computing per day usage of library', 'text5': 'Document No',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_2_6 = ('status',)
# --------------------------* 4.3.1 *--------------------------------------- OK
fc4_3_1 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc4_3_1 = {'date': 'Year', 'text1': 'IT Facilities', 'text2': 'Installation Date',
           'text3': 'Nature of Updation', 'text4': 'Date of Updation', 'text5': 'Arrangements for Updation',
           'text6': 'Expenditure on Updation', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_3_1 = ('status',)
# --------------------------* 4.3.2 *--------------------------------------- OK
fc4_3_2 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc4_3_2 = {'date': 'Year', 'text1': 'Total No. of Students', 'text2': 'No. of Computers',
           'text3': 'No. of Computers in working Condition', 'text4': 'No of Linux OS', 'text5': 'Document No',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_3_2 = ('status',)
# --------------------------* 4.3.3 *---------------------------------------
fc4_3_3 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc4_3_3 = {'cid': '4.3.3', 'date': 'Year', 'text1': '>/= 50 Mbps', 'text2': '35-50 Mbps', 'text3': '20-35 Mbps',
           'text4': '5-20 Mbps', 'text5': '< 5 Mbps', 'text6': 'Document No', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc4_3_3 = ('status',)
# --------------------------* 4.3.4 *---------------------------------------
fc4_3_4 = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc4_3_4 = {'date': 'Year', 'text1': 'Name of the E-content', 'text2': 'Facilities for E-content development',
           'text3': 'Link', 'text4': 'Document No', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc4_3_4 = ('status',)
# --------------------------* 4.4.1 *---------------------------------------
fc4_4_1 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc4_4_1 = {'date': 'Year', 'text1': 'Heads of Expenditure on Academic support facilities',
           'text2': 'Expenditure on maintenance on academic facilities (Rs in Lakhs)',
           'text3': 'Heads of expenditure on maintenance on physical facilities ',
           'text4': 'Expenditure on maintenance on physical facilities (Rs in Lakhs)',
           'text5': 'Document Number',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc4_4_1 = ('status',)
# --------------------------* 4.4.2 *---------------------------------------
fc4_4_2 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc4_4_2 = {'date': 'Year', 'text1': 'Facilities', 'text2': 'Type of Facility ',
           'text3': 'System for the maintenance', 'text4': 'Amount for Maintenance ', 'text5': 'System for utilization',
           'text6': 'Others', 'text8': 'Document No', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc4_4_2 = ('status',)
# --------------------------* 5.1.1 *---------------------------------------
fc5_1_1 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc5_1_1 = {'date': 'Year', 'department': 'Department', 'text2': 'Name of the Scheme',
           'text3': 'No. of Students Benefited by scholarships', 'text4': 'No. of Students Benefited by freeships',
           'text5': 'Document No', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_1 = ('department', 'status',)
# --------------------------* 5.1.2 *---------------------------------------
fc5_1_2 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc5_1_2 = {'date': 'Year', 'department': 'Department', 'text2': 'Class', 'text3': 'Name of the Scheme',
           'text4': 'Scheme Providers address with phone number', 'text5': 'No. of Students Benefited by scholarships',
           'text6': 'No. of Students Benefited by freeships', 'text8': 'Document No',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_2 = ('department', 'status',)

# --------------------------* 5.1.3A *---------------------------------------
fc5_1_3A = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc5_1_3A = {'date': 'Year', 'department': 'Department', 'text2': 'Year of implementation ',
            'text3': 'No. of Students Enrolled', 'text4': 'Program Detail',
            'text5': 'Name & Address of Agencies involved', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc5_1_3A = ('department', 'status',)

# --------------------------* 5.1.3B *---------------------------------------
fc5_1_3B = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc5_1_3B = {'date': 'Year', 'department': 'Department', 'text2': 'Year of implementation ',
            'text3': 'No. of Students Enrolled', 'text4': 'Program details',
            'text5': 'Name & Address of Agencies involved',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_3B = ('department', 'status',)

# --------------------------* 5.1.3C *---------------------------------------
fc5_1_3C = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc5_1_3C = {'date': 'Year', 'department': 'Department', 'text2': 'Year of implementation ',
            'text3': 'No. of Students Enrolled', 'text4': 'Program Details',
            'text5': 'Name & Address of Agencies involved', 'text6': 'Document No.',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_3C = ('department', 'status',)

# --------------------------* 5.1.3D *---------------------------------------
fc5_1_3D = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc5_1_3D = {'date': 'Year', 'text1': 'Year of implementation ', 'text2': 'Details of Program',
            'text3': 'Name & Address of Agencies involved', 'text4': 'Document No.',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_3D = ('status',)

# --------------------------* 5.1.3E *---------------------------------------
fc5_1_3E = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc5_1_3E = {'date': 'Year', 'text1': 'Year of implementation ', 'text2': 'No. of Students Enrolled',
            'text3': 'Name & Address of Agencies involved', 'text4': 'Document No.',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_3E = ('status',)

# --------------------------* 5.1.3F *---------------------------------------
fc5_1_3F = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc5_1_3F = {'date': 'Year', 'text1': 'Year of implementation ', 'text2': 'No. of Students Enrolled',
            'text3': 'Name & Address of Agencies involved', 'text4': 'Document No.',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_3F = ('status',)

# --------------------------* 5.1.3G *---------------------------------------
fc5_1_3G = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc5_1_3G = {'date': 'Year', 'text1': 'Year of implementation ', 'text2': 'No. of Students Enrolled',
            'text3': 'Program Detail', 'text4': 'Name & Address of Agencies involved',
            'text5': 'Document No.', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_3G = ('status',)

# --------------------------* 5.1.3H *---------------------------------------
fc5_1_3H = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc5_1_3H = {'date': 'Year', 'text1': 'Year of implementation', 'text2': 'No. of Students Enrolled',
            'text3': 'Name & Address of Agencies involved', 'text4': 'Document No',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_3H = ('status',)

# --------------------------* 5.1.4 *---------------------------------------
fc5_1_4 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc5_1_4 = {'date': 'Year', 'department': 'Department', 'text2': 'Name of the Scheme',
           'text3': 'No. of students attended the guidance for competitive examinations',
           'text4': 'No. of students benefited the guidance for competitive examinations',
           'text5': 'No. of students attended the Career Counselling',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_4 = ('department', 'status',)
# --------------------------* 5.1.5 *---------------------------------------
fc5_1_5 = ('date', 'department', 'text2', 'text3', 'text4', 'file1', 'url1')
dc5_1_5 = {'date': 'Year', 'department': 'Department', 'text2': 'Name of the Scheme ',
           'text3': 'No. of Students attended', 'text4': 'No. of Students Benefited',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_5 = ('status',)
# --------------------------* 5.1.6 *---------------------------------------
fc5_1_6 = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc5_1_6 = {'date': 'Year', 'text1': 'No.of Grievances Appealed', 'text2': 'No.of Grievance Redressed',
           'text3': 'Average time for grievance re-dressal (No of days)', 'text4': 'Document No',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_1_6 = ('status',)

# --------------------------* 5.2.1 *---------------------------------------
fc5_2_1 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc5_2_1 = {'date': 'Year', 'department': 'Department', 'text2': 'Name of students placed', 'text3': 'Class',
           'text4': 'On campus/off campus', 'text5': 'Designation/Post',
           'text6': 'Name of the employer with contact detail',
           'text8': 'Package received', 'text9': 'Program graduated from', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc5_2_1 = ('status',)

# --------------------------* 5.2.2 *---------------------------------------
fc5_2_2 = ('date', 'department', 'program', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc5_2_2 = {'cid': '5.2.2', 'date': 'Year', 'department': 'Department', 'program': 'Programme',
           'text3': 'Name of the student',
           'text4': '(UG to PG / PG TO M.Phil  / M.Phil to Ph.D / PG to P.hD / Ph.D to Post Doctoral)',
           'text5': 'Program Joined', 'text6': 'Name of the institution joined',
           'text8': 'Address & Contact details of institution joined', 'text9': 'Document No',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_2_2 = ('department', 'program', 'status',)

# --------------------------* 5.2.3 *---------------------------------------
fc5_2_3 = ('date', 'department', 'program', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc5_2_3 = {'date': 'Year', 'department': 'Department', 'program': 'Program', 'text3': 'Name of student',
           'text4': 'Register number / Roll no of Exam',
           'text5': 'Attended (NET/SET/SLET/GATE/GMAT/CAT/GRE/JAM/IELTS/TOEFL/ Other equivalent examinations / IAS / UPSC / PSC)',
           'text6': 'Qualified (NET/SET/SLET/GATE/GMAT/CAT/GRE/JAM/IELTS/TOEFL/ Other equivalent examinations / IAS / UPSC / PSC)',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_2_3 = ('department', 'program', 'status',)

# --------------------------* 5.3.1 *---------------------------------------
fc5_3_1 = ('date', 'text1', 'program', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10', 'file1', 'url1')
dc5_3_1 = {'date': 'Year', 'text1': 'Department ', 'program': 'Program', 'text3': 'Student Name',
           'text4': 'Sports (Event) ', 'text5': 'Cultural (Event)', 'text6': 'Name of the Award / Medal',
           'text8': 'National / International', 'text9': 'Aadhar or Student id No', 'text10': 'Document No',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_3_1 = ('department', 'program', 'status',)
# --------------------------* 5.3.2 A *---------------------------------------
fc5_3_2A = ('date', 'text1', 'department', 'text3', 'text4', 'text5', 'file1', 'url1')
dc5_3_2A = {'date': 'Year', 'text1': 'Name of the Bodies', 'department': 'Department',
            'text3': 'Name of Students ', 'text4': 'Position held', 'text5': 'Document No',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_3_2A = ('department', 'status',)
# --------------------------* 5.3.2 B *---------------------------------------
fc5_3_2B = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc5_3_2B = {'date': 'Year', 'department': 'Department', 'text2': 'Name of the Activity',
            'text3': 'Academic / Non Academic', 'text4': 'Purpose', 'text5': 'Chief Guest or resource person',
            'text6': 'If it’s a competition, name of the winners and prize money',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc5_3_2B = ('department', 'status',)
# --------------------------* 5.3.3 *---------------------------------------
fc5_3_3 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc5_3_3 = {'date': 'Year', 'department': 'Department', 'text2': 'Name of Event', 'text3': 'Sports / Cultural',
           'text4': 'No. of Participants', 'text5': 'Document No', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc5_3_3 = ('department', 'status',)
# --------------------------* 5.4.2 *---------------------------------------
fc5_4_2 = ('date', 'text1', 'department', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10',
           'text11', 'file1', 'url1')
dc5_4_2 = {'date': 'Year', 'text1': 'Name of the Alumni', 'department': 'Department',
           'text3': 'Registered Alumni or not', 'text4': 'Aadhar / PAN', 'text5': 'Year of graduation',
           'text6': 'Year of Contribution', 'text8': 'Quantum of Contribution ', 'text9': 'Purpose ',
           'text10': 'Non Financial Contribution ', 'text11': 'Purpose', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc5_4_2 = ('department', 'status',)
# --------------------------* 5.4.3A *---------------------------------------
fc5_4_1A = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc5_4_1A = {'date': 'Year', 'department': 'Department', 'text2': 'Program',
            'text3': 'Total No. of Alumni enrolled ', 'text4': 'No. of Alumni Association meetings', 'text5': 'Purpose',
            'text6': 'Date of Alumni meeting', 'text8': 'No. of members attended',
            'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc5_4_1A = ('status',)
# --------------------------* 5.4.3 B *---------------------------------------
fc5_4_1B = ('date', 'date2', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc5_4_1B = {'date': 'Year', 'date2': 'Date of Chapter meeting', 'text1': 'Name of the Chapter ',
            'text2': 'Total No. of Members enrolled ', 'text3': 'No. of Chapter meetings ', 'text4': 'Purpose',
            'text5': 'No. of members attended', 'text6': 'Venue', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc5_4_1B = ('status',)

# --------------------------* 6.1.1 *---------------------------------------
fc6_1_1 = ('date', 'file1', 'url1')
dc6_1_1 = {'date': 'Year', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_1_1 = ('status',)
# --------------------------* 6.1.2 *---------------------------------------
fc6_1_2 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc6_1_2 = {'date': 'Year', 'text1': 'Name of the practice', 'text2': 'Strategic Plan',
           'text3': 'Description of the practice', 'text4': 'No.of Members involved ',
           'text5': 'Type of members', 'text6': 'Activities', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc6_1_2 = ('status',)
# --------------------------* 6.2.1 *--------------------

fc6_2_1 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc6_2_1 = {'date': 'Year', 'text1': 'Activity', 'text2': 'Strategic plan', 'text3': 'Implementation',
           'text4': 'Outcome', 'text5': 'Plan / Deployment document ', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc6_2_1 = ('status',)
# --------------------------* 6.2.2 *---------------------------------------
fc6_2_2 = ('date', 'file1', 'url1')
dc6_2_2 = {'cid': '6.2.2', 'date': 'Year', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_2_2 = ('status',)

# --------------------------* 6.2.3 *---------------------------------------
fc6_2_3 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc6_2_3 = {'date': 'Year', 'text1': 'Area of E-governance',
           'text2': 'Name of the vendor with contact details ', 'text3': 'Year of implementations',
           'text4': 'Details of Implementation', 'text5': 'Document submitted', 'text6': 'Document No',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_2_3 = ('department', 'status',)

# --------------------------* 6.2.4 *---------------------------------------
fc6_2_4 = (
    'date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'text10', 'file1', 'url1')
dc6_2_4 = {'date': 'Year', 'department': 'Department / Bodies / Cells / Committees', 'text2': 'activity',
           'text3': 'Date of decision as per minutes', 'text4': 'Date of activity implementation date',
           'text5': 'Implementation of the activity', 'text6': 'Resource Persons', 'text8': 'Faculty In-charge',
           'text9': 'No. of Beneficiaries', 'text10': 'Outcome', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc6_2_4 = ('department', 'status',)
# --------------------------* 6.3.1 *---------------------------------------
fc6_3_1 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc6_3_1 = {'date': 'Year', 'text1': 'Welfare measures for teaching', 'text2': 'No of  beneficiaries',
           'text3': 'Welfare measures for Non -teaching', 'text4': 'No of  beneficiaries',
           'text5': 'Additional information ', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc6_3_1 = ('status',)
# --------------------------* 6.3.2 *---------------------------------------
fc6_3_2 = ('date', 'text1', 'department', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc6_3_2 = {'date': 'Year', 'text1': 'Name of the faculty', 'department': 'Department', 'text3': ' Designation ',
           'text4': 'PAN Number', 'text5': 'Conferences / Workshops / Professional bodies / Seminar',
           'text6': 'Title of conferences / Workshops / Name of the Professional Body',
           'text8': 'National / International / Regional', 'text9': 'Amount of support /Membership Fee of bodies',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_3_2 = ('department', 'status',)
# --------------------------* 6.3.3 *---------------------------------------
fc6_3_3 = ('date', 'text1', 'text2', 'text3', 'date2', 'date3', 'text6', 'text8', 'file1', 'url1')
dc6_3_3 = {'date': 'Year', 'text1': 'Title of professional development program organised',
           'text2': 'Teaching / Non-Teaching', 'text3': 'Resource Person With Contact Details',
           'date2': 'Date From ', 'date3': 'Date To', 'text6': 'No of participants ', 'text8': 'Outcome',
           'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc6_3_3 = ('status',)
# --------------------------* 6.3.4 *---------------------------------------
fc6_3_4 = ('date', 'text1', 'text2', 'text3', 'date4', 'date5', 'text6', 'text8', 'text9', 'text10', 'file1', 'url1')
dc6_3_4 = {'date': 'Year', 'text1': 'Name of faculty ', 'department': 'Department', 'text3': 'Designation',
           'text4': 'Type of the course', 'date2': 'Date from', 'date3': 'Date to', 'text8': 'Conducting Agency',
           'text9': 'No. of days', 'text10': 'Document No', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc6_3_4 = ('department', 'status',)
# --------------------------* 6.3.5 *---------------------------------------
fc6_3_5 = ('date', 'file1', 'url1')
dc6_3_5 = {'date': 'Year', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_3_5 = ('status',)
# --------------------------* 6.4.1 *---------------------------------------
fc6_4_1 = ('date', 'date2', 'text1', 'text2', 'text3', 'file1', 'url1')
dc6_4_1 = {'date': 'Year', 'date2': 'Date', 'text1': 'Type of Financial Audit (Internal / External) ',
           'text2': 'Remarks', 'text3': 'Mechanism for settling audit objections',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_4_1 = ('status',)
# --------------------------* 6.4.2 *---------------------------------------
fc6_4_2 = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc6_4_2 = {'cid': '6.4.2', 'date': 'Year', 'text1': 'Name of Non government funding agencies / individuals',
           'text2': 'Funds or grants received  (Amount)', 'text3': 'Purpose', 'text4': 'Initiative taken',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_4_2 = ('status',)
# --------------------------* 6.4.3 *---------------------------------------
fc6_4_3 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc6_4_3 = {'cid': '6.4.3', 'date': 'Year', 'text1': 'Strategy for mobilising fund',
           'text2': 'Source of mobilising funds', 'text3': 'Funds raised ', 'text4': 'Heads of optimal utilisation',
           'text5': 'Amount utilised', 'text6': 'Outcome',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_4_3 = ('status',)
# --------------------------* 6.4.5 *---------------------------------------
fc6_4_5 = ('date', 'text1', 'text2', 'text3', 'file1', 'url1')
dc6_4_5 = {'date': 'Year', 'text1': 'Practices institutionalised ', 'text2': 'Process', 'text3': 'Outcome',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_4_5 = ('status',)
# --------------------------* 6.5.1 *---------------------------------------
fc6_5_1 = ('date', 'text1', 'text2', 'text3', 'file1', 'url1')
dc6_5_1 = {'date': 'Year', 'text1': 'Practices institutionalised ', 'text2': 'Process', 'text3': 'Outcome',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_5_1 = ('status',)
# --------------------------* 6.5.2 *---------------------------------------
fc6_5_2 = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc6_5_2 = {'date': 'Year', 'text1': 'Teaching Learning Process',
           'text2': 'Structure & Methodologies of operation', 'text3': 'Learning Outcomes',
           'text4': 'Reforms  implemented',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_5_2 = ('status',)
# --------------------------* 6.5.3 *---------------------------------------
fc6_5_3 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc6_5_3 = {'date': 'Year', 'text1': 'Name of the quality initiative', 'text2': 'Description',
           'text3': 'Duration from  ', 'text4': 'Duration to ', 'text5': 'No of Participants', 'text6': 'Outcome',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_5_3 = ('status',)
# --------------------------* 6.5.4 *---------------------------------------
fc6_5_4 = ('date', 'date2', 'text1', 'text2', 'text3', 'file1', 'url1')
dc6_5_4 = {'date': 'Year', 'date2': 'Renewal Date', 'text1': 'Type',
           'text2': 'Participants / Agency / Resource person', 'text3': 'Remarks',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc6_5_4 = ('status',)
# --------------------------* 6.5.5 *---------------------------------------
fc6_5_5 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc6_5_5 = {'date': 'Year', 'text1': 'Quality enhancement programs ',
           'text2': 'Academic domain / Administrative domains', 'text3': 'Date of implementation',
           'text4': 'No. of Beneficiaries ', 'text5': 'Remarks', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc6_5_5 = ('status',)
# --------------------------* 7.1.1 *---------------------------------------
fc7_1_1 = (
    'date', 'department', 'text2', 'text3', 'text4', 'date2', 'date3', 'text5', 'text6', 'text8', 'file1', 'url1')
dc7_1_1 = {'date': 'Year', 'date2': 'Date from', 'date3': 'Date to', 'department': 'Department',
           'text2': 'Title of the program ', 'text3': 'Resource person ', 'text4': 'Activities',
           'text5': 'No of participants (Male)', 'text6': 'No of participants (Female)', 'text8': 'Report',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_1 = ('department', 'status',)
# --------------------------* 7.1.2 A *---------------------------------------
fc7_1_2A = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc7_1_2A = {'date': 'Year', 'department': 'Department', 'text2': 'Measures Taken ',
            'text3': 'No. of Beneficiaries', 'text4': 'Grievances registered', 'text5': 'Grievances addressed',
            'text6': 'Time taken for redressing ', 'text8': 'Impact ', 'text9': 'Remarks',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_2A = ('department', 'status',)
# --------------------------* 7.1.2 B *---------------------------------------
fc7_1_2B = ('date', 'department', 'text2', 'text3', 'text4', 'file1', 'url1')
dc7_1_2B = {'date': 'Year', 'department': 'Department', 'text2': 'Measures Taken',
            'text3': 'No. of Beneficiaries', 'text4': 'Remarks', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc7_1_2B = ('department', 'status',)
# --------------------------* 7.1.2 C *---------------------------------------
fc7_1_2C = ('date', 'text1', 'file1', 'url1')
dc7_1_2C = {'date': 'Year', 'text1': 'Common Room / Other Facilities',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_2C = ('status',)
# --------------------------* 7.1.3 *---------------------------------------
fc7_1_3 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc7_1_3 = {'date': 'Year', 'text1': 'Power Requirement met by renewable energy sources',
           'text2': 'Total Power requirement', 'text3': 'Renewable energy source',
           'text4': 'Renewable energy generated and used', 'text5': 'Energy supplied to the grid',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_3 = ('status',)
# --------------------------* 7.1.4 *---------------------------------------
fc7_1_4 = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc7_1_4 = {'date': 'Year', 'text1': 'Lighting requirements (KWh) ',
           'text2': 'Requirement met through LED bulbs (Kwh)', 'text3': 'Percentage lighting through LED bulbs ',
           'text4': 'Percentage lighting through other sources', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc7_1_4 = ('status',)
# --------------------------* 7.1.5 *---------------------------------------
fc7_1_5 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc7_1_5 = {'date': 'Year', 'text1': 'SOLID /LIQUID / E-WASTE MANAGEMENT', 'text2': 'Measure Taken',
           'text3': 'Year of Implementation', 'text4': 'Method of processing', 'text5': 'Initial Investment',
           'text6': 'Working Expense', 'text8': 'Working Expense excluding salary', 'text9': 'Impact',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_5 = ('status',)
# --------------------------* 7.1.6 *---------------------------------------
fc7_1_6 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc7_1_6 = {'date': 'Year', 'text1': 'Measures Taken', 'text2': 'Year of implementation', 'text3': 'Process',
           'text4': 'Capacity in Litre', 'text5': 'Initial Investment', 'text6': 'Working Expense',
           'text8': 'No. of Beneficiaries / Purpose', 'text9': 'Impact', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc7_1_6 = ('status',)
# --------------------------* 7.1.7 A *---------------------------------------
fc7_1_7A = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'text9', 'file1', 'url1')
dc7_1_7A = {'date': 'Year', 'department': 'Department', 'text2': 'Measures Taken',
            'text3': 'No. of Trees Planted', 'text4': 'Details of Trees ', 'text5': 'Expenses Incurred for planting',
            'text6': 'Expenses for maintaining', 'text8': 'Expenses for maintaining Excluding Salary',
            'text9': 'Impact',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_7A = ('department', 'status',)
# --------------------------* 7.1.7 B *---------------------------------------
fc7_1_7B = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc7_1_7B = {'date': 'Year', 'text1': 'Measures Taken', 'text2': 'Process', 'text3': 'Investment',
            'text4': 'Working Expense', 'text5': 'Groups Involved (NSS, NCC, etc.,)', 'text6': 'Impact',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_7B = ('status',)
# --------------------------* 7.1.7 C *---------------------------------------
fc7_1_7C = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc7_1_7C = {'date': 'Year', 'text1': 'Students / Staff', 'text2': 'Bicycles', 'text3': 'Public Transport',
            'text4': 'Pedestrian friendly roads', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc7_1_7C = ('status',)
# --------------------------* 7.1.7 D *---------------------------------------
fc7_1_7D = ('date', 'text1', 'text2', 'text3', 'file1', 'url1')
dc7_1_7D = {'date': 'Year', 'text1': 'Year of Implementation', 'text2': 'Methods Implemented',
            'text3': 'Result', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_7D = ('status',)
# --------------------------* 7.1.8 *---------------------------------------
fc7_1_8 = ('date', 'date2', 'text1', 'file1', 'url1')
dc7_1_8 = {'date': 'Year', 'date2': 'Date of Green Audit', 'text1': 'Report',
           'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_8 = ('status',)
# --------------------------* 7.1.9 *---------------------------------------
fc7_1_9 = ('date', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc7_1_9 = {'date': 'Year', 'text1': 'Facilities', 'text2': 'No of resources',
           'text3': 'No. of beneficiaries ', 'text4': 'Remarks', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc7_1_9 = ('status',)
# --------------------------* 7.1.10 *---------------------------------------
fc7_1_10 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc7_1_10 = {'date': 'Year', 'text1': 'Advantages (Description)', 'text2': 'Disadvantages (Description)',
            'text3': 'Initiative Taken', 'text4': 'Process of initiatives', 'text5': 'No. of Beneficiaries',
            'text6': 'Impact', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_10 = ('status',)
# --------------------------* 7.1.11 *---------------------------------------
fc7_1_11 = ('date', 'date2', 'date3', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc7_1_11 = {'date': 'Year', 'date2': 'Date from', 'date3': 'Date to', 'text1': 'Issues addressed',
            'text2': 'Name of initiatives', 'text3': 'No. of Students Participated',
            'text4': 'No. & Category of Local Beneficiaries', 'text5': 'Outcome',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_11 = ('status',)
# --------------------------* 7.1.12 *---------------------------------------
fc7_1_12 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc7_1_12 = {'date': 'Date', 'text1': 'Hand book for students', 'text2': 'Hand book for teachers',
            'text3': 'Hand book for governing body', 'text4': 'Hand book for Administration',
            'text5': 'Principal / Supporting Staff', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc7_1_12 = ('status',)
# --------------------------* 7.1.13 *---------------------------------------
fc7_1_13 = ('date', 'file1', 'url1')
dc7_1_13 = {'date': 'Date', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_13 = ('status',)
# --------------------------* 7.1.14 *---------------------------------------
fc7_1_14 = ('date', 'date2', 'date3', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc7_1_14 = {'date': 'Year', 'date2': 'Duration from ', 'date3': 'Duration to',
            'text1': 'Title of the program', 'text2': 'Resource person', 'text3': 'No. & Category of beneficiaries',
            'text4': 'Report ', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_14 = ('status',)
# --------------------------* 7.1.15 *---------------------------------------
fc7_1_15 = ('date', 'department', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc7_1_15 = {'date': 'Year of Implementation', 'department': 'Department', 'text2': 'Course', 'text3': 'Duration',
            'text4': 'No. of Beneficiaries', 'text5': 'Impact', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc7_1_15 = ('department', 'status',)
# --------------------------* 7.1.16 *---------------------------------------
fc7_1_16 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc7_1_16 = {'date': 'Year', 'text1': 'Functions ', 'text2': 'Suggestions ', 'text3': 'Bodies',
            'text4': 'Level of implementation', 'text5': 'Impact', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc7_1_16 = ('status',)
# --------------------------* 7.1.17 *---------------------------------------
fc7_1_17 = (
    'date', 'date2', 'date3', 'department', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc7_1_17 = {'date': 'Year', 'date2': 'Duration from', 'date3': 'Duration to ', 'department': 'Department',
            'text1': 'Title of program / activity', 'text2': 'No. of participants',
            'text3': 'Code of conduct for students ',
            'text4': 'Code of conduct for teachers',
            'text5': 'handbooks /Manuals / Brochures on human values and professional ethics',
            'text6': 'Report on the student attributes', 'file1': 'Additional Information Files',
            'url1': 'Additional Info Link'}
sc7_1_17 = ('department', 'status',)
# --------------------------* 7.1.18 *---------------------------------------
# Department
fc7_1_18 = ('date', 'department', 'text1', 'text2', 'text3', 'text4', 'text5', 'file1', 'url1')
dc7_1_18 = {'date': 'Year', 'department': 'Department', 'text1': 'Event', 'text2': 'No.of Participants',
            'text3': 'Guest / Resource person', 'text4': 'Content covered', 'text5': 'Remarks',
            'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_18 = ('department', 'status',)
# --------------------------* 7.1.19 *---------------------------------------
fc7_1_19 = ('date', 'date2', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'file1', 'url1')
dc7_1_19 = {'date': 'Year', 'date2': 'Date of training program ', 'text1': 'Type of function ',
            'text2': 'Methods adopted', 'text3': 'Date of audit', 'text4': 'Result ', 'text5': 'Training Programs',
            'text6': 'No. of Participants', 'file1': 'Additional Information Files', 'url1': 'Additional Info Link'}
sc7_1_19 = ('status',)
# --------------------------* 7.2.1 *---------------------------------------
# Department
fc7_2_1 = ('date', 'department', 'text1', 'text2', 'text3', 'text4', 'file1', 'url1')
dc7_2_1 = {'date': 'Year', 'department': 'Department', 'text1': 'Best Practice', 'text2': 'Method of operation',
           'text3': 'Category of beneficiaries', 'text4': 'No. of beneficiaries',
           'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc7_2_1 = ('department', 'status',)
# --------------------------* 7.3.1 *---------------------------------------
fc7_3_1 = ('date', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text8', 'file1', 'url1')
dc7_3_1 = {'date': 'Year ', 'text1': 'Activity / Area', 'text2': 'Distinctiveness',
           'text3': 'Method of operation', 'text4': 'No. of Participants / Beneficiaries ', 'text5': 'External Sources',
           'text6': 'Internal Sources', 'text8': 'Result', 'file1': 'Additional Information Files',
           'url1': 'Additional Info Link'}
sc7_3_1 = ('status',)

# For importing to AutoUpdate.generator.create for Automatically Generate HTML files based on Fields in this dict.
all_field_keys = {"c1_1_1": fc1_1_1[:-2], "c1_1_2": fc1_1_2[:-2], "c1_1_3": fc1_1_3[:-2],
                  "c1_2_1": fc1_2_1[:-2], "c1_2_2": fc1_2_2[:-2], "c1_3_1": fc1_3_1[:-2], "c1_3_2": fc1_3_2[:-2],
                  "c1_3_3": fc1_3_3[:-2], "c1_3_4": fc1_3_4[:-2], "c1_4_1": fc1_4_1[:-2], "c1_4_2": fc1_4_2[:-2],
                  "c2_1_1": fc2_1_1[:-2], "c2_1_2": fc2_1_2[:-2], "c2_1_3": fc2_1_3[:-2], "c2_2_1": fc2_2_1[:-2],
                  "c2_2_2": fc2_2_2[:-2], "c2_2_3": fc2_2_3[:-2], "c2_3_1": fc2_3_1[:-2], "c2_3_2": fc2_3_2[:-2],
                  "c2_3_3": fc2_3_3[:-2], "c2_3_4": fc2_3_4[:-2], "c2_4_1": fc2_4_1[:-2], "c2_4_2": fc2_4_2[:-2],
                  "c2_4_3": fc2_4_3[:-2], "c2_4_4": fc2_4_4[:-2], "c2_4_5": fc2_4_5[:-2], "c2_5_1": fc2_5_1[:-2],
                  "c2_5_2": fc2_5_2[:-2], "c2_5_3": fc2_5_3[:-2], "c2_5_4": fc2_5_4[:-2], "c2_5_5": fc2_5_5[:-2],
                  "c2_6_1": fc2_6_1[:-2], "c2_6_2": fc2_6_2[:-2], "c2_6_3": fc2_6_3[:-2], "c2_7_1": fc2_7_1[:-2],
                  "c3_1_1": fc3_1_1[:-2], "c3_1_2": fc3_1_2[:-2], "c3_1_3": fc3_1_3[:-2], "c3_1_4": fc3_1_4[:-2],
                  "c3_2_1": fc3_2_1[:-2], "c3_2_2": fc3_2_2[:-2], "c3_2_3": fc3_2_3[:-2], "c3_2_4": fc3_2_4[:-2],
                  "c3_3_1": fc3_3_1[:-2], "c3_3_2": fc3_3_2[:-2], "c3_3_3": fc3_3_3[:-2], "c3_4_1": fc3_4_1[:-2],
                  "c3_4_2": fc3_4_2[:-2], "c3_4_3": fc3_4_3[:-2], "c3_4_4": fc3_4_4[:-2], "c3_4_5": fc3_4_5[:-2],
                  "c3_4_6": fc3_4_6[:-2], "c3_4_7": fc3_4_7[:-2], "c3_4_8": fc3_4_8[:-2], "c3_5_1": fc3_5_1[:-2],
                  "c3_5_2": fc3_5_2[:-2], "c3_5_3": fc3_5_3[:-2], "c3_6_1": fc3_6_1[:-2], "c3_6_2": fc3_6_2[:-2],
                  "c3_6_3": fc3_6_3[:-2], "c3_6_4": fc3_6_4[:-2], "c3_7_1": fc3_7_1[:-2], "c3_7_2": fc3_7_2[:-2],
                  "c3_7_3": fc3_7_3[:-2], "c4_1_1": fc4_1_1[:-2], "c4_1_2A": fc4_1_2A[:-2], "c4_1_2B": fc4_1_2B[:-2],
                  "c4_1_2C": fc4_1_2C[:-2], "c4_1_2D": fc4_1_2D[:-2], "c4_1_2E": fc4_1_2E[:-2],
                  "c4_1_3": fc4_1_3[:-2], "c4_1_4": fc4_1_4[:-2], "c4_2_1": fc4_2_1[:-2], "c4_2_2": fc4_2_2[:-2],
                  "c4_2_3": fc4_2_3[:-2], "c4_2_4": fc4_2_4[:-2], "c4_2_5": fc4_2_5[:-2], "c4_2_6": fc4_2_6[:-2],
                  "c4_3_1": fc4_3_1[:-2], "c4_3_2": fc4_3_2[:-2], "c4_3_3": fc4_3_3[:-2], "c4_3_4": fc4_3_4[:-2],
                  "c4_4_1": fc4_4_1[:-2], "c4_4_2": fc4_4_2[:-2], "c5_1_1": fc5_1_1[:-2], "c5_1_2": fc5_1_2[:-2],
                  "c5_1_3A": fc5_1_3A[:-2], "c5_1_3B": fc5_1_3B[:-2], "c5_1_3C": fc5_1_3C[:-2],
                  "c5_1_3D": fc5_1_3D[:-2], "c5_1_3E": fc5_1_3E[:-2], "c5_1_3F": fc5_1_3F[:-2],
                  "c5_1_3G": fc5_1_3G[:-2],
                  "c5_1_3H": fc5_1_3H[:-2], "c5_1_4": fc5_1_4[:-2], "c5_1_5": fc5_1_5[:-2], "c5_1_6": fc5_1_6[:-2],
                  "c5_2_1": fc5_2_1[:-2], "c5_2_2": fc5_2_2[:-2], "c5_2_3": fc5_2_3[:-2], "c5_3_1": fc5_3_1[:-2],
                  "c5_3_2A": fc5_3_2A[:-2], "c5_3_2B": fc5_3_2B[:-2], "c5_3_3": fc5_3_3[:-2],
                  "c5_4_1A": fc5_4_1A[:-2], "c5_4_1B": fc5_4_1B[:-2], "c5_4_2": fc5_4_2[:-2], "c6_1_1": fc6_1_1[:-2],
                  "c6_1_2": fc6_1_2[:-2], "c6_2_1": fc6_2_1[:-2], "c6_2_2": fc6_2_2[:-2], "c6_2_3": fc6_2_3[:-2],
                  "c6_2_4": fc6_2_4[:-2], "c6_3_1": fc6_3_1[:-2], "c6_3_2": fc6_3_2[:-2], "c6_3_3": fc6_3_3[:-2],
                  "c6_3_4": fc6_3_4[:-2], "c6_3_5": fc6_3_5[:-2], "c6_4_1": fc6_4_1[:-2], "c6_4_2": fc6_4_2[:-2],
                  "c6_4_3": fc6_4_3[:-2], "c6_5_1": fc6_5_1[:-2], "c6_5_2": fc6_5_2[:-2], "c6_5_3": fc6_5_3[:-2],
                  "c6_5_4": fc6_5_4[:-2], "c6_5_5": fc6_5_5[:-2], "c7_1_1": fc7_1_1[:-2], "c7_1_2A": fc7_1_2A[:-2],
                  "c7_1_2B": fc7_1_2B[:-2], "c7_1_2C": fc7_1_2C[:-2], "c7_1_3": fc7_1_3[:-2], "c7_1_4": fc7_1_4[:-2],
                  "c7_1_5": fc7_1_5[:-2], "c7_1_6": fc7_1_6[:-2], "c7_1_7A": fc7_1_7A[:-2], "c7_1_7B": fc7_1_7B[:-2],
                  "c7_1_7C": fc7_1_7C[:-2], "c7_1_7D": fc7_1_7D[:-2], "c7_1_8": fc7_1_8[:-2], "c7_1_9": fc7_1_9[:-2],
                  "c7_1_10": fc7_1_10[:-2], "c7_1_11": fc7_1_11[:-2], "c7_1_12": fc7_1_12[:-2],
                  "c7_1_13": fc7_1_13[:-2],
                  "c7_1_14": fc7_1_14[:-2], "c7_1_15": fc7_1_15[:-2], "c7_1_16": fc7_1_16[:-2],
                  "c7_1_17": fc7_1_17[:-2],
                  "c7_1_18": fc7_1_18[:-2], "c7_1_19": fc7_1_19[:-2], "c7_2_1": fc7_2_1[:-2], "c7_3_1": fc7_3_1[:-2]}

# For importing to Criteria.criterion for Automatically Generate HTML Table Headers based on Fields in this dict.
all_field_values = {"c1_1_1": dc1_1_1, "c1_1_2": dc1_1_2, "c1_1_3": dc1_1_3, "c1_2_1": dc1_2_1, "c1_2_2": dc1_2_2,
                    "c1_3_1": dc1_3_1, "c1_3_2": dc1_3_2, "c1_3_3": dc1_3_3, "c1_3_4": dc1_3_4, "c1_4_1": dc1_4_1,
                    "c1_4_2": dc1_4_2, "c2_1_1": dc2_1_1, "c2_1_2": dc2_1_2, "c2_1_3": dc2_1_3, "c2_2_1": dc2_2_1,
                    "c2_2_2": dc2_2_2, "c2_2_3": dc2_2_3, "c2_3_1": dc2_3_1, "c2_3_2": dc2_3_2, "c2_3_3": dc2_3_3,
                    "c2_3_4": dc2_3_4, "c2_4_1": dc2_4_1, "c2_4_2": dc2_4_2, "c2_4_3": dc2_4_3, "c2_4_4": dc2_4_4,
                    "c2_4_5": dc2_4_5, "c2_5_1": dc2_5_1, "c2_5_2": dc2_5_2,
                    "c2_5_3": dc2_5_3, "c2_5_4": dc2_5_4, "c2_5_5": dc2_5_5, "c2_6_1": dc2_6_1, "c2_6_2": dc2_6_2,
                    "c2_6_3": dc2_6_3, "c2_7_1": dc2_7_1, "c3_1_1": dc3_1_1, "c3_1_2": dc3_1_2, "c3_1_3": dc3_1_3,
                    "c3_1_4": dc3_1_4, "c3_2_1": dc3_2_1, "c3_2_2": dc3_2_2, "c3_2_3": dc3_2_3, "c3_2_4": dc3_2_4,
                    "c3_3_1": dc3_3_1, "c3_3_2": dc3_3_2, "c3_3_3": dc3_3_3, "c3_4_1": dc3_4_1, "c3_4_2": dc3_4_2,
                    "c3_4_3": dc3_4_3, "c3_4_4": dc3_4_4, "c3_4_5": dc3_4_5, "c3_4_6": dc3_4_6, "c3_4_7": dc3_4_7,
                    "c3_4_8": dc3_4_8, "c3_5_1": dc3_5_1, "c3_5_2": dc3_5_2, "c3_5_3": dc3_5_3, "c3_6_1": dc3_6_1,
                    "c3_6_2": dc3_6_2, "c3_6_3": dc3_6_3, "c3_6_4": dc3_6_4, "c3_7_1": dc3_7_1, "c3_7_2": dc3_7_2,
                    "c3_7_3": dc3_7_3, "c4_1_1": dc4_1_1, "c4_1_2A": dc4_1_2A, "c4_1_2B": dc4_1_2B,
                    "c4_1_2C": dc4_1_2C, "c4_1_2D": dc4_1_2D,
                    "c4_1_2E": dc4_1_2E, "c4_1_3": dc4_1_3, "c4_1_4": dc4_1_4, "c4_2_1": dc4_2_1, "c4_2_2": dc4_2_2,
                    "c4_2_3": dc4_2_3, "c4_2_4": dc4_2_4, "c4_2_5": dc4_2_5, "c4_2_6": dc4_2_6, "c4_3_1": dc4_3_1,
                    "c4_3_2": dc4_3_2, "c4_3_3": dc4_3_3, "c4_3_4": dc4_3_4, "c4_4_1": dc4_4_1, "c4_4_2": dc4_4_2,
                    "c5_1_1": dc5_1_1, "c5_1_2": dc5_1_2, "c5_1_3A": dc5_1_3A, "c5_1_3B": dc5_1_3B,
                    "c5_1_3C": dc5_1_3C, "c5_1_3D": dc5_1_3D, "c5_1_3E": dc5_1_3E, "c5_1_3F": dc5_1_3F,
                    "c5_1_3G": dc5_1_3G, "c5_1_3H": dc5_1_3H, "c5_1_4": dc5_1_4,
                    "c5_1_5": dc5_1_5, "c5_1_6": dc5_1_6, "c5_2_1": dc5_2_1, "c5_2_2": dc5_2_2, "c5_2_3": dc5_2_3,
                    "c5_3_1": dc5_3_1, "c5_3_2A": dc5_3_2A, "c5_3_2B": dc5_3_2B, "c5_3_3": dc5_3_3,
                    "c5_4_1A": dc5_4_1A, "c5_4_1B": dc5_4_1B, "c5_4_2": dc5_4_2, "c6_1_1": dc6_1_1, "c6_1_2": dc6_1_2,
                    "c6_2_1": dc6_2_1, "c6_2_2": dc6_2_2, "c6_2_3": dc6_2_3, "c6_2_4": dc6_2_4, "c6_3_1": dc6_3_1,
                    "c6_3_2": dc6_3_2, "c6_3_3": dc6_3_3, "c6_3_4": dc6_3_4, "c6_3_5": dc6_3_5, "c6_4_1": dc6_4_1,
                    "c6_4_2": dc6_4_2, "c6_4_3": dc6_4_3, "c6_5_1": dc6_5_1, "c6_5_2": dc6_5_2, "c6_5_3": dc6_5_3,
                    "c6_5_4": dc6_5_4, "c6_5_5": dc6_5_5,
                    "c7_1_1": dc7_1_1, "c7_1_2A": dc7_1_2A, "c7_1_2B": dc7_1_2B, "c7_1_2C": dc7_1_2C, "c7_1_3": dc7_1_3,
                    "c7_1_4": dc7_1_4, "c7_1_5": dc7_1_5, "c7_1_6": dc7_1_6, "c7_1_7A": dc7_1_7A, "c7_1_7B": dc7_1_7B,
                    "c7_1_7C": dc7_1_7C, "c7_1_7D": dc7_1_7D, "c7_1_8": dc7_1_8, "c7_1_9": dc7_1_9,
                    "c7_1_10": dc7_1_10, "c7_1_11": dc7_1_11, "c7_1_12": dc7_1_12, "c7_1_13": dc7_1_13,
                    "c7_1_14": dc7_1_14, "c7_1_15": dc7_1_15, "c7_1_16": dc7_1_16, "c7_1_17": dc7_1_17,
                    "c7_1_18": dc7_1_18,
                    "c7_1_19": dc7_1_19, "c7_2_1": dc7_2_1, "c7_3_1": dc7_3_1}
