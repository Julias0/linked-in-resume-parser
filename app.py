from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
experience_section= False

experiences = []

for page_layout in extract_pages("linkedin_resume.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            experience_instance = {}
            for text_line in element:
                if 'Experience' in text_line.get_text():
                    # print(text_line.get_text())
                    experience_section = True 

                if 'Education' in text_line.get_text():
                   experience_section = False 

                if experience_section:
                    # print(text_line.get_text())
                    for character in text_line:
                        if isinstance(character, LTChar):
                            if character.size == 12 and len(text_line.get_text().strip()) > 0:
                                print('Company: ' + text_line.get_text())
                                experience_instance['Company'] = text_line.get_text()
                                break


                            if character.size == 11.5 and len(text_line.get_text().strip()) > 0:
                                print('Role: ' + text_line.get_text())
                                experience_instance['Role'] = text_line.get_text()
                                break

                            got_duration = True
                            for month in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
                                if len(text_line.get_text().strip()) > 0 and month in text_line.get_text().lower():
                                   print('Duration: ' + text_line.get_text())
                                   experience_instance['Duration'] = text_line.get_text()
                                   got_duration = True
                                   break
                                
                            if got_duration:
                                break
            if len(experience_instance.keys()) > 0:
                experiences.append(experience_instance)


print(experiences)