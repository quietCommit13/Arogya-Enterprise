import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    font_names = ["segoeuib.ttf" if bold else "segoeui.ttf", 
                  "arialbd.ttf" if bold else "arial.ttf", 
                  "calibrib.ttf" if bold else "calibri.ttf"]
    for name in font_names:
        font_path = os.path.join("C:\\Windows\\Fonts", name)
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def create_sample_lab_report():
    width = 1000
    height = 1350
    image = Image.new("RGB", (width, height), color="#FFFFFF")
    draw = ImageDraw.Draw(image)

    # Colors
    c_primary = "#0D47A1"      # Deep Hospital Blue
    c_secondary = "#1565C0"    # Medium Blue
    c_alert = "#D32F2F"        # Alert Red
    c_warn = "#E65100"         # Alert Amber
    c_text = "#212121"         # Dark Charcoal
    c_muted = "#616161"        # Muted Gray
    c_border = "#BDBDBD"       # Light Gray Border
    c_bg_light = "#F5F7FA"     # Soft Table BG
    c_alert_bg = "#FFEBEE"     # Soft Red BG

    font_h1 = get_font(26, bold=True)
    font_h2 = get_font(18, bold=True)
    font_h3 = get_font(15, bold=True)
    font_body = get_font(14, bold=False)
    font_bold = get_font(14, bold=True)
    font_small = get_font(12, bold=False)
    font_small_bold = get_font(12, bold=True)

    # Top Header Banner
    draw.rectangle([(0, 0), (width, 110)], fill=c_primary)
    draw.text((width // 2, 28), "GOVERNMENT OF INDIA - NATIONAL HEALTH MISSION", fill="#FFFFFF", font=font_small_bold, anchor="mm")
    draw.text((width // 2, 58), "DISTRICT CIVIL HOSPITAL & COMMUNITY HEALTH CENTRE", fill="#FFFFFF", font=font_h1, anchor="mm")
    draw.text((width // 2, 90), "CENTRAL PATHOLOGY & DIAGNOSTIC LABORATORY (NABL ACCREDITED LAB #MC-4029)", fill="#E3F2FD", font=font_small, anchor="mm")

    # Patient Details Box
    draw.rectangle([(40, 130), (width - 40, 260)], outline=c_border, width=2, fill="#FAFAFA")
    
    # Left column details
    y = 145
    draw.text((60, y), "Patient Ref ID:", fill=c_muted, font=font_small)
    draw.text((180, y), "PT-2026-89", fill=c_text, font=font_bold)

    draw.text((450, y), "Age / Gender:", fill=c_muted, font=font_small)
    draw.text((560, y), "34 Yrs / Female", fill=c_text, font=font_bold)

    draw.text((750, y), "Lab Reg No:", fill=c_muted, font=font_small)
    draw.text((840, y), "CHC-LAB-4491", fill=c_text, font=font_bold)

    y += 35
    draw.text((60, y), "Patient Name:", fill=c_muted, font=font_small)
    draw.text((180, y), "Sunita Sharma (UHID: 9812-4410)", fill=c_text, font=font_bold)

    draw.text((450, y), "Referred By:", fill=c_muted, font=font_small)
    draw.text((560, y), "Dr. K. Verma, MO (PHC OPD)", fill=c_text, font=font_bold)

    draw.text((750, y), "Sample Type:", fill=c_muted, font=font_small)
    draw.text((840, y), "Whole Blood (EDTA)", fill=c_text, font=font_body)

    y += 35
    draw.text((60, y), "Collection Time:", fill=c_muted, font=font_small)
    draw.text((180, y), "07-Oct-2026  08:45 AM", fill=c_text, font=font_body)

    draw.text((450, y), "Reporting Time:", fill=c_muted, font=font_small)
    draw.text((560, y), "07-Oct-2026  10:15 AM", fill=c_text, font=font_body)

    draw.text((750, y), "Clinical Status:", fill=c_muted, font=font_small)
    draw.text((840, y), "OPD Urgent Triage", fill=c_alert, font=font_bold)

    # Title of Report
    draw.text((width // 2, 290), "COMPLETE BLOOD COUNT (CBC) & FEBRILE SEROLOGY REPORT", fill=c_secondary, font=font_h2, anchor="mm")
    draw.line([(40, 310), (width - 40, 310)], fill=c_secondary, width=2)

    # Table Header
    y_table = 325
    draw.rectangle([(40, y_table), (width - 40, y_table + 35)], fill="#ECEFF1")
    draw.text((60, y_table + 10), "TEST PARAMETER", fill=c_text, font=font_h3)
    draw.text((360, y_table + 10), "OBSERVED VALUE", fill=c_text, font=font_h3)
    draw.text((550, y_table + 10), "REFERENCE RANGE", fill=c_text, font=font_h3)
    draw.text((740, y_table + 10), "UNITS", fill=c_text, font=font_h3)
    draw.text((860, y_table + 10), "FLAG STATUS", fill=c_text, font=font_h3)

    # Table Rows
    rows = [
        ("Hemoglobin (Hb)", "8.2", "12.0 - 15.0", "g/dL", "LOW (Moderate)", True, c_alert_bg, c_alert),
        ("Total Leukocyte Count (TLC / WBC)", "3,400", "4,000 - 11,000", "/cu.mm", "LOW (Leukopenia)", True, "#FFF8E1", c_warn),
        ("Platelet Count (PLT)", "45,000", "150,000 - 450,000", "/cu.mm", "CRITICAL LOW", True, c_alert_bg, c_alert),
        ("Packed Cell Volume (PCV / Hematocrit)", "26.4", "36.0 - 46.0", "%", "LOW", True, "#FFF8E1", c_warn),
        ("RBC Count", "3.10", "3.80 - 4.80", "mill/cu.mm", "LOW", False, None, c_muted),
        ("Mean Corpuscular Volume (MCV)", "85.2", "80.0 - 99.0", "fL", "NORMAL", False, None, c_muted),
        ("Mean Corpuscular Hb (MCH)", "26.5", "27.0 - 32.0", "pg", "BORDERLINE", False, None, c_muted),
        ("Dengue NS1 Antigen Rapid Test", "REACTIVE (+)", "Non-Reactive", "-", "POSITIVE (+)", True, c_alert_bg, c_alert),
        ("Dengue IgM Antibodies", "REACTIVE (+)", "Non-Reactive", "-", "POSITIVE (+)", True, c_alert_bg, c_alert),
        ("Malaria Smear & RDT (Pv / Pf)", "NEGATIVE", "Negative", "-", "NORMAL", False, None, c_muted),
        ("Widal Slide Agglutination", "NEGATIVE (TO/TH < 1:80)", "Negative", "-", "NORMAL", False, None, c_muted),
        ("Random Blood Sugar (RBS)", "104", "70 - 140", "mg/dL", "NORMAL", False, None, c_muted),
    ]

    curr_y = y_table + 38
    row_height = 45
    for test, val, ref, unit, flag, is_abnormal, bg_color, flag_color in rows:
        if bg_color:
            draw.rectangle([(40, curr_y), (width - 40, curr_y + row_height - 2)], fill=bg_color)
        else:
            if (curr_y // row_height) % 2 == 0:
                draw.rectangle([(40, curr_y), (width - 40, curr_y + row_height - 2)], fill="#FAFAFA")
        
        # Draw bottom line
        draw.line([(40, curr_y + row_height - 1), (width - 40, curr_y + row_height - 1)], fill="#E0E0E0", width=1)

        draw.text((60, curr_y + 12), test, fill=c_text, font=font_bold if is_abnormal else font_body)
        draw.text((360, curr_y + 12), val, fill=c_alert if is_abnormal else c_text, font=font_bold if is_abnormal else font_body)
        draw.text((550, curr_y + 12), ref, fill=c_muted, font=font_body)
        draw.text((740, curr_y + 12), unit, fill=c_muted, font=font_body)
        
        # Badge for Flag
        if is_abnormal:
            draw.rectangle([(845, curr_y + 8), (955, curr_y + 34)], fill=flag_color)
            draw.text((900, curr_y + 13), flag[:12], fill="#FFFFFF", font=font_small_bold, anchor="mm")
        else:
            draw.text((860, curr_y + 12), flag, fill="#4CAF50", font=font_small_bold)

        curr_y += row_height

    # Clinical Interpretation Box
    curr_y += 15
    draw.rectangle([(40, curr_y), (width - 40, curr_y + 140)], fill="#FFF3E0", outline="#FFB74D", width=2)
    draw.text((60, curr_y + 15), "PATHOLOGIST REMARKS & CRITICAL ALERT SUMMARY:", fill="#B71C1C", font=font_h3)
    remarks = [
        "1. CRITICAL THROMBOCYTOPENIA: Platelet count at 45,000 /cu.mm (< 50,000 threshold for inpatient fever triage).",
        "2. Positive Dengue NS1 & IgM indicates acute primary Dengue infection with vascular risk.",
        "3. Concomitant Anemia: Hemoglobin 8.2 g/dL. Watch for mucosal bleeding, hematuria, or sudden BP drop.",
        "4. URGENT CLINICAL RECOMMENDATION: Immediate Medical Officer evaluation for IV fluid protocol or tertiary referral."
    ]
    rem_y = curr_y + 45
    for r in remarks:
        draw.text((60, rem_y), r, fill="#37474F", font=font_small)
        rem_y += 22

    # Signatures & Verification Area
    curr_y += 165
    draw.line([(40, curr_y), (width - 40, curr_y)], fill=c_border, width=1)
    curr_y += 20
    
    # Left Sign
    draw.text((80, curr_y), "R. K. Murthy, DMLT", fill=c_text, font=font_bold)
    draw.text((80, curr_y + 20), "Senior Medical Lab Technician", fill=c_muted, font=font_small)
    draw.text((80, curr_y + 40), "Govt. Civil Hospital Lab", fill=c_muted, font=font_small)

    # Center QR/Barcode simulation
    draw.rectangle([(width // 2 - 80, curr_y), (width // 2 + 80, curr_y + 45)], outline=c_border, fill="#ECEFF1")
    draw.text((width // 2, curr_y + 22), "*CHC-2026-4491*", fill=c_muted, font=font_small_bold, anchor="mm")

    # Right Sign
    draw.text((720, curr_y), "Dr. Priya Sengupta, MD", fill=c_text, font=font_bold)
    draw.text((720, curr_y + 20), "Consultant Pathologist & HOD", fill=c_muted, font=font_small)
    draw.text((720, curr_y + 40), "Reg. No: MCI-2014-48201", fill=c_muted, font=font_small)

    # Disclaimer Footer
    draw.rectangle([(0, height - 45), (width, height)], fill="#263238")
    draw.text((width // 2, height - 22), "NON-DIAGNOSTIC LAB RECORD COPY | FOR MEDICAL OFFICER CLINICAL EVALUATION ONLY", fill="#CFD8DC", font=font_small_bold, anchor="mm")

    # Save output
    output_path = os.path.join(os.getcwd(), "sample_lab_report.png")
    image.save(output_path, "PNG", quality=95)
    print(f"Sample lab report successfully generated at: {output_path}")

if __name__ == "__main__":
    create_sample_lab_report()
