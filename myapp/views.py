
# views.py

from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Image, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

# from .forms import CandidateForm, ReportForm
from reportlab.lib.units import inch
import PyPDF2



pdfmetrics.registerFont(TTFont('Times-Bold', 'studentproject/fonts/times-new-roman-grassetto.ttf'))

def generate_report_pdf(request):
    if request.method == 'POST':
            # form=ReportForm(request.POST)
                projectTitle=request.POST.get('projectTitle')
                teamLeaderName=request.POST.get('teamLeaderName', '')
                candidate1=request.POST.get('candidate1', '')
                candidate2=request.POST.get('candidate2', '')
                candidate3=request.POST.get('candidate3', '')
                teamLeaderRegNo=request.POST.get('teamLeaderRegNo', '')
                candidate1RegNo=request.POST.get('candidate1RegNo', '')
                candidate2RegNo=request.POST.get('candidate2RegNo', '')
                candidate3RegNo=request.POST.get('candidate3RegNo', '')
                branch =request.POST.get('branch', '')
                degree=request.POST.get('degree', '')
                college = request.POST.get('college', '')
                abstract = request.POST.get('abstract','')
                justificationsdg = request.POST.get('justificationsdg', '')
                justificationsap = request.POST.get('justificationsap', '')
                acceleration = request.POST.get('acceleration', '')
                designing = request.POST.get('designing', '')
                bootcamp = request.POST.get('bootcamp', '')
                business = request.POST.get('business','')
                # print(candidate1)
                


            

            # request.post
        # formset = formset_factory(CandidateForm, extra=1)(request.POST)
       
            # if  form.is_valid():
                title = projectTitle.upper()
                project_report = 'A LIVE IN LAB REPORT'.upper()
                submittedby_text = 'Submitted by'
                text1 = 'in partial fulfillment for the award of the degree'
                text2='of'
                text3='IN'
                text4='An Autonomous Institution: Affiliated to Anna University,\
              Chennai-600025'
                candidate_name = teamLeaderName.upper()
                award_degree = degree.upper()
                branch_study = branch.upper()
                college_name = college.upper()
                university = "Anna University".upper()
                month_year = "2023".upper()
                subjectcode="01982y".upper()
                labname="Live in lab".upper()
                
              
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="project_report.pdf"'

            # Create the SimpleDocTemplate for the first page
                doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
            # Prepare the elements for the first page
                elements = [] #page1
                elements_second_page=[] #page2
                styles = getSampleStyleSheet()
                table_data = [[Image('studentproject/assets/sit.png', width=100, height=100),Spacer(150,50), Image('studentproject/assets/anna.png', width=100, height=100)]]
                table = Table(table_data)
                table.setStyle(TableStyle([('ALIGN', (1, 1), (-1, -1), 'CENTER', 'MIDDLE')]))  # Center align both images
                elements.append(table)
            
            
            
        # Add image to the story
        #     elements.append(img)
        #     image_path = 'studentproject/assets/sit.png'  # Update with the actual image path
        #     img = Image(image_path, width=200, height=150)

        #     elements.append(img)  
                elements.append(Paragraph(title,  ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=18, fontName='Times-Bold', alignment=TA_CENTER, leading=20)))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(project_report, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=14, fontName='Times-Bold',alignment=TA_CENTER)))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(submittedby_text,ParagraphStyle(name='ItalicStyle', parent=styles['Italic'],fontSize=14, fontName='Times-Italic',alignment=TA_CENTER)))
                elements.append(Spacer(1, 20))
                #candidate names
                elements.append(Paragraph(candidate_name, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold', leading=1.5,alignment=TA_CENTER)))
                elements.append(Spacer(1, 20))
                # for candidate_form in formset:
                #     print(candidate_form)
                #     if candidate_form.is_valid():
                #         candidate_name = candidate_form.cleaned_data.get('candidate_name', '').upper()
                #         # You can extract other candidate details similarly...

                #         # Create Paragraph elements and append them to the elements list
                elements.append(Paragraph(candidate_name, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold', leading=1.5, alignment=TA_CENTER)))
                # elements.append(Spacer(1, 20))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(text1,ParagraphStyle(name='ItalicStyle', parent=styles['Italic'],fontSize=14, fontName='Times-Italic',leading=1.5,alignment=TA_CENTER)))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(text2,ParagraphStyle(name='ItalicStyle', parent=styles['Italic'], fontSize=14,fontName='Times-Italic',leading=1.5,alignment=TA_CENTER)))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(award_degree, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',alignment=TA_CENTER)))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(text3, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=14, fontName='Times-Bold',alignment=TA_CENTER)))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(branch_study, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=14, fontName='Times-Bold',alignment=TA_CENTER)))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(college_name, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=14, fontName='Times-Bold',alignment=TA_CENTER)))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(text4, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=12, fontName='Times-Bold',alignment=TA_CENTER,leading=1.5)))
                elements.append(Spacer(1, 20))
                elements.append(Paragraph(university, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=1.5,alignment=TA_CENTER)))
                elements.append(Spacer(1, 70))
                elements.append(Paragraph(month_year, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=14, fontName='Times-Bold',leading=1.5,alignment=TA_CENTER)))
                elements.append(PageBreak())
                


            #second page
            
             
                bonafide_cert = 'BONAFIDE CERTIFICATE'
                cert_content = f'Certified that this project report "{title}" is the bonafide work of "{project_report}" '\
                    f'who carried out "{subjectcode}" - "{labname}" the project work under my supervision.'
                submitted=f'Submitted for project Viva - Voce Examination held on ____________'
                examiner1=f'INTERNAL EXAMINER'.upper()
                examiner2=f'EXTERNAL EXAMINER'.upper()

        #     signature_line = '<<Signature of the Head of the Department>> <<Signature of the Supervisor>>\n' \
        #              '<<Name>> <<Name>>\n' \
        #              '<<Academic Designation>>\n' \
        #              '<<Department>> <<Department>>\n' \
        #     
        #              '<<Full addrsess of the Dept & College >> <<Full address of the Dept & College >>'
                data = [
                    [Paragraph('SIGNATURE',
                            ParagraphStyle(
                    name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=1.5,),
                ), Spacer(80,10), Paragraph('SIGNATURE',ParagraphStyle(
                    name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=1.5,)),Spacer(80,10), Paragraph('SIGNATURE',ParagraphStyle(
                    name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=1.5,))],
                    [Paragraph('Guide',ParagraphStyle(
                    name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=1.5,)),Spacer(80,10), Paragraph('Lab in Charge',ParagraphStyle(
                    name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=20,)),Spacer(80,10), Paragraph('HOD',ParagraphStyle(
                    name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=1.5,))],
                    ]
                table = Table(data,colWidths=[110, 120, 110])
                data1=[
                    [
                        Paragraph(examiner1,ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=16)),
                        
                        Paragraph(examiner2,ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=16))
                    ],
                    
                ]
                table2=Table(data1)

        # Add style to the table (for even spacing)
            
            
                elements_second_page.append(Paragraph(college_name,ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',leading=1.5,alignment=TA_CENTER)))
                elements_second_page.append(Spacer(1, 25))
                elements_second_page.append(Paragraph(text4, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=12, fontName='Times-Bold',leading=1.5,alignment=TA_CENTER)))
                elements_second_page.append(Spacer(1, 50))
                elements_second_page.append(Paragraph(bonafide_cert, ParagraphStyle(name='TitleStyle', parent=styles['Normal'], fontSize=18, fontName='Times-Bold', alignment=TA_CENTER)))
                elements_second_page.append(Spacer(1, 36))
                elements_second_page.append(Paragraph(cert_content, ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=16, fontName='Times-Roman',leading=27)))
                elements_second_page.append(Spacer(1, 90))
                elements_second_page.append(table)
                elements_second_page.append(Spacer(8, 60))
                elements_second_page.append(Paragraph(submitted, ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=16, fontName='Times-Roman',leading=27)))
                elements_second_page.append(Spacer(1,40))
                
                elements_second_page.append(table2)
                elements_second_page.append(PageBreak())
            



            #third page
                elements_third_page=[]
                elements_third_page.append(Paragraph("ABSTRACT", ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=18, fontName='Times-Bold',alignment=TA_CENTER)))
                elements_third_page.append(Spacer(20,20))
                elements_third_page.append(Paragraph(title, ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',alignment=TA_CENTER)))

                elements_third_page.append(PageBreak())

            


                #table of contents page
                table_of_contents=[]
                table=[
                    [
                        Paragraph("S.NO",ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=18, fontName='Times-Bold',alignment=TA_CENTER)),
                        
                        Paragraph("TITLE",ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=18, fontName='Times-Bold',alignment=TA_CENTER)),
                        
                        Paragraph("PAGE NO.",ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=18, fontName='Times-Bold',alignment=TA_CENTER,leading=18)),

                    ]
                ]
                


                data=Table(table,colWidths=[185,190,300])


                words_to_be_searched=['Problem Statement','Origin of the Problem','Motivation to do this project','Beneficiary of the final product','Case Studies','Literature Survey','Mind Map / Fishbone Diagram / Algorithm','Architectural Diagram','Functional and Non Functional Requirements','Hardware and Software Requirements','Online Course Certification / Seminar attended','Business Model Development','Business Model Canvas','Final PPT (In line with POSITIVE Score)','Sairam SDG Solveathon 2.0 Certificate (if any) /Proof for Levels Cleared (Screen shot from InnovationEcosystem Portal)','Student Activity File Index Sheet','REFERENCES']

                
                table_of_contents.append(data)
                table_of_contents.append(Spacer(10,18))
                table_of_contents.append(tableofcontents_tile(sno='1',title='ACCELERATION',styles=styles))
                table_of_contents.append(Spacer(7,18))
                table_of_contents.append(tableofcontents_subtile(sno='1.1',title='Problem Statement',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='1.2',title='Origin of the Problem',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='1.3',title='Motivation to do this project',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='1.4',title='Beneficiary of the final product',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='1.5',title='Case Studies',styles=styles))
                table_of_contents.append(Spacer(10,18))
                table_of_contents.append(tableofcontents_tile(sno='2',title='DESIGN THINKING',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='2.1',title='Literature Survey',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='2.2',title='Mind Map / Fishbone Diagram / Algorithm',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='2.3',title='Architectural Diagram',styles=styles))
                table_of_contents.append(Spacer(10,18))
                table_of_contents.append(tableofcontents_tile(sno='3',title='BOOTCAMP',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='3.1',title='Functional and Non Functional Requirements',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='3.2',title='Hardware and Software Requirements',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='3.3',title='Online Course Certification / Seminar attended',styles=styles))
                table_of_contents.append(Spacer(10,18))
                table_of_contents.append(tableofcontents_tile(sno='4',title='BUSINESS MODEL',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='4.1',title='Business Model Development ',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='4.2',title='Business Model Canvas',styles=styles))
                table_of_contents.append(Spacer(10,18))
                table_of_contents.append(tableofcontents_subtile(sno='5',title='FINAL PPT  (In line with POSITIVE Score)',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='6',title='Sairam SDG Solveathon 2.0 Certificate (if any) /Proof for Levels Cleared (Screen shot from InnovationEcosystem Portal',styles=styles))
                table_of_contents.append(tableofcontents_subtile(sno='7',title='Student Activity File Index Sheet',styles=styles))
                table_of_contents.append(Spacer(10,18))
                table_of_contents.append(tableofcontents_subtile(sno='8',title='REFERENCES',styles=styles))
                table_of_contents.append(Spacer(10,18))
                table_of_contents.append(PageBreak())

                table_data = [
                [  Paragraph("S.No"),Paragraph("Title"),Paragraph("Date of Completion"),Paragraph("Mark (Out of 10)"),Paragraph("Remarks"),Paragraph("Signature of the Faculty")],
                    [Paragraph("1"), Paragraph("Acceleration"), '', '', '', ''],
                    [Paragraph("1.1"), Paragraph("Problem Statement (Minimum Three Versions)")],
                    [Paragraph("1.2"), Paragraph("Origin of the Problem, Motivation to do this project & Beneficiary of the final product")],
                    [Paragraph("1.3"), Paragraph("Case Studies")],
                    [Paragraph("2"), Paragraph("Design Thinking"), '', '', '', ''],
                    [Paragraph("2.1"), Paragraph("Literature Survey (Description, advantages and limitations of the individual Paper and Summary)")],
                    [Paragraph("2.2"), Paragraph("Mind Map / Fishbone Diagram / Algorithm")],
                    [Paragraph("2.3"), Paragraph("Block Diagram / Architectural Diagram")],
                    [Paragraph("3"), Paragraph("Bootcamp"), '', '', '', ''],
                    [Paragraph("3.1"), Paragraph("Requirements  (Functional, Nonfunctional, Tools / Hardware & Software)  identified to solve the problem")],
                    [Paragraph("3.2"), Paragraph("Outcome of Bootcamp / Technological Training (write up & Certificate)")],
                    [Paragraph("4"), Paragraph("Business Model"), '', '', '', ''],
                    [Paragraph("4.1"), Paragraph("Business Model Canvas")],
                    [Paragraph("5"), Paragraph("Proof for Self Learning (Online Course Participation / Seminar or Webinar attended)")],
                    [Paragraph("6"), Paragraph("Review Paper & Final PPT (Justification for POSITIVE - Productable, Opportunities, Sustainable, Informative, Technology, Innovative, Viable & Ethical)")]
                 ]

                #accleration Page
                page_1=[]
                page_1.append(Paragraph("Sairam SDG Solveathon 2.0", ParagraphStyle(
                name='Normal', parent=styles['Normal'], fontSize=18, fontName='Times-Bold', alignment=TA_CENTER)))
                page_1.append(Spacer(1, 20))
                column_widths = [0.5 * inch, 2.5 * inch, 1.0 * inch, 0.7 * inch, 1.0 * inch, 1.0 * inch]
                table = Table(table_data,colWidths=column_widths)
                max_lines_per_row = []
                for row in table_data:
                    max_lines = max([len(str(cell).split('\n')) for cell in row])
                    max_lines_per_row.append(max_lines)
                # table._argW[3] = 2.5*inch

    # Iterate through the table data to calculate the maximum lines per row

                style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            # ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('SPAN',(1,1),(5,1)),
            ('SPAN',(1,5),(5,5)),
            ('SPAN',(1,9),(5,9)),
            ('SPAN',(1,12),(5,12)),
        ])
                table.setStyle(style,)

        # Add the table to the elements list
                page_1.append(table)

                elements.extend(elements_second_page)
                elements.extend(elements_third_page)
                elements.extend(table_of_contents)
                elements.extend(page_1)
                

                

                # Build the PDF with the elements for the first page
                doc.build(elements)

                # Provide the paths to the original PDF, the page to insert, and the output PDF
                # original_pdf_path = ''
                # page_to_insert_path = 'page_to_insert.pdf'
                # output_pdf_path = 'output.pdf'
                
                # # Specify the page number where you want to insert the new page
                # page_number_to_insert = 2

                # Insert the page into the original PDF
                # insert_page(original_pdf_path, page_to_insert_path, output_pdf_path, page_number_to_insert)

                


                return response
    else:
                # form = ReportForm()
                # formset=formset_factory(CandidateForm,extra=3)()

        return render(request, 'generate_report_pdf.html', )




def tableofcontents_tile(sno,title,styles):
    
    table=[
                [   
                    
                    Paragraph(f'{sno}',style=ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',),),
                
                    Paragraph(f'{title}',style=ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=16, fontName='Times-Bold',),),
                   
                ]
            ]
    return Table(table,colWidths=[70, 400])

def tableofcontents_subtile(sno,title,styles):
    
    table=[
                [
                    Spacer(1,20),
                    Paragraph(f'{sno}',style=ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=12, fontName='Times-Bold',)),
                    # Spacer(1,2),
                    Paragraph(f'{title}',style=ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=12, fontName='Times-Bold',)),
                    
                    Paragraph("1")
                ]
            ]
    return Table(table, ident=0, colWidths=[280, 70, 290, 300])


def insert_page(pdf_path, page_path, output_path, page_number):
    # Open the original PDF and the page to insert
    with open(pdf_path, 'rb') as pdf_file, open(page_path, 'rb') as page_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page_pdf = PyPDF2.PdfFileReader(page_file)

        # Create a new PDF writer
        pdf_writer = PyPDF2.PdfFileWriter()

        # Add the original pages up to the page number where you want to insert the new page
        for page_index in range(page_number):
            page = pdf_reader.getPage(page_index)
            pdf_writer.addPage(page)

        # Add the new page from the page PDF
        page = page_pdf.getPage(0)
        pdf_writer.addPage(page)

        # Add the remaining original pages
        for page_index in range(page_number, pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_index)
            pdf_writer.addPage(page)

        # Write the modified PDF to the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)