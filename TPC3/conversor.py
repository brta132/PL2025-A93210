import re
import sys

def main(mark_file_path):

    # abrir ficheiro teste
    with open(mark_file_path, "r") as markfile:
        with open("html.txt", "w+") as htmlFile:

            # set regex
            r_headings = r"^(?P<heading>#{1,6})(?P<h_cont>.*)$"
            r_list_ord = r"^(?P<ident>\s*)\d+\.(?P<list_ord_cont>.*)$"
            r_list_unord = r"^(?P<ident_un>\s*)[-+*](?P<list_un_cont>.*)$"
            r_h_list = re.compile(rf"{r_headings}|{r_list_ord}|{r_list_unord}")

            r_image = r"^!\[(?P<image_name>.*)\]\((?P<image_link>.*)\)$"
            r_link = r"\[(?P<link_name>.*?)\]\((?P<link>.*?)\)"
            r_img_lnk = re.compile(rf"{r_image}|{r_link}")

            r_b_it_imp = r"([*_])([*_])?([*_])?(?P<b_it_cont>.*?)(?P<em_c>\3?\2?\1)"
            r_emph = re.compile(r_b_it_imp)
            
            # match regex
            match_found = False

            last_line_list = False
            list_type = "" # what type was the last line
            list_n = 0 # how many open list tags have been opened so far, but not closed
            list_ident = ""
            while line := markfile.readline():

                if(line.isspace() and last_line_list):
                    htmlFile.writelines(f"</{list_type}>\n")
                    last_line_list = False
                    list_type = ""
                    list_n = 0
                    list_ident = ""

                # Substitute Bold, Italics and Emphasis
                for match in r_emph.finditer(line):
                    
                    size = len(match.group('em_c'))
                    
                    type_b_start = "<b><i>"
                    type_b_end = "</i></b>"
                    if(size == 1):
                        type_b_start = "<i>"
                        type_b_end = "</i>"
                    
                    elif (size == 2):
                        type_b_start = "<b>"
                        type_b_end = "</b>"


                    sub_str = f"{type_b_start}{match.group('b_it_cont')}{type_b_end}"
                    line = re.sub(r_b_it_imp,sub_str,line,count=1)
                    
                    match_found = True

                # Substitute Images and Links
                for match in r_img_lnk.finditer(line):
                    # Substitute Image (Full Line)
                    if("image_name" in match.groupdict() and match.group("image_name") is not None):
                        sub_str = f"<img src=\"{match.group("image_link")}\" alt=\"{match.group("image_name")}\"/>"
                        line = re.sub(r_image, sub_str, line, count=1)

                    # Substitute links
                    else:
                        sub_str = f"<a href=\"{match.group("link")}\">{match.group("link_name")}</a>"
                        line = re.sub(r_link,sub_str,line,count=1)
                    
                    match_found = True

                # Substitute Headings, Ordered Lists and Unordered Lists
                for match in r_h_list.finditer(line):
                   
                    # Substitute headings
                    if "h_cont" in match.groupdict() and match.group('h_cont') is not None:

                        # close list if last line was list
                        if(last_line_list):
                            htmlFile.writelines(f"</{list_type}>\n")
                            list_n -= 1
                            if(list_n == 0): 
                                list_type = ""
                                list_ident = ""

                        l = len(str(match.group("heading")))
                        sub_str = f"<h{l}>{match.group("h_cont")}</h{l}>"

                        line = re.sub(r_headings, sub_str, line, count=1)

                    # Substitute ordered lists
                    elif "list_ord_cont" in match.groupdict() and match.group('list_ord_cont') is not None:
                        
                        sub_str = ""

                        # check if start of list block
                        if(not last_line_list):
                            sub_str += "<ol>\n"
                            list_n += 1

                        # check if ident is diferent from last
                        if len(match.group("ident")) > len(list_ident):
                            sub_str += f"{match.group("ident")}<ol>\n"
                            list_n += 1

                        elif len(match.group("ident")) < len(list_ident):
                            sub_str += f"{list_ident}</{list_type}>\n"
                            list_n -= 1

                        sub_str += f"{match.group("ident")}\t<li>\n{match.group("ident")}\t\t{match.group('list_ord_cont')}\n{match.group("ident")}\t</li>"

                        line = re.sub(r_list_ord, sub_str, line, count=1)
                        
                        last_line_list = True
                        list_type = "ol"
                        list_ident = match.group("ident")


                    # Substitute unordered lists
                    else:
                       
                        sub_str = ""

                        # check if start of list block
                        if(not last_line_list):
                            sub_str += "<ul>\n"
                            list_n += 1


                        # check if ident is diferent from last
                        if len(match.group("ident_un")) > len(list_ident):
                            sub_str += f"{match.group("ident_un")}<ul>\n"
                            list_n += 1

                        elif len(match.group("ident_un")) < len(list_ident):
                            sub_str += f"{list_ident}</{list_type}>\n"
                            list_n -= 1

                        sub_str += f"{match.group("ident_un")}\t<li>\n{match.group("ident_un")}\t\t{match.group('list_un_cont')}\n{match.group("ident_un")}\t</li>"

                        line = re.sub(r_list_unord, sub_str, line, count=1)
                        
                        last_line_list = True
                        list_type = "ul"
                        list_ident = match.group("ident_un")
 
                    # htmlFile.writelines(str(match.groupdict()))
                    match_found = True

                # List has stopped: last line was part of a list, but this one isn't
                if(last_line_list and not match_found):
                    htmlFile.writelines(f"</{list_type}>")
                    list_n -= 1
                    last_line_list = False
                    if(list_n == 0): 
                        list_type = ""
                        list_ident = ""
                                      

                htmlFile.write(''.join([line, '\n']))               

    return


if __name__ == "__main__":
    main(sys.argv[1])
