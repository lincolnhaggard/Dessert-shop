from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

def make_receipt(data,out_file_name):
    pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )
    styles = getSampleStyleSheet() 