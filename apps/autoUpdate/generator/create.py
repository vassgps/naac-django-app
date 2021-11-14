# AutoUpdate/generator/create.py
from django.http import HttpResponse
from ...criterions.fields.field_names import all_field_keys, all_field_values

all_criterion = ["c1_1_1", "c1_1_2", "c1_1_3", "c1_2_1", "c1_2_2", "c1_3_1", "c1_3_2",
                 "c1_3_3", "c1_3_4", "c1_4_1", "c1_4_2", "c2_1_1", "c2_1_2", "c2_1_3",
                 "c2_2_1", "c2_2_2", "c2_2_3", "c2_3_1", "c2_3_2", "c2_3_3", "c2_3_4",
                 "c2_4_1", "c2_4_2", "c2_4_3", "c2_4_4", "c2_4_5", "c2_5_1", "c2_5_2",
                 "c2_5_3", "c2_5_4", "c2_5_5", "c2_6_1", "c2_6_2", "c2_6_3", "c2_7_1",
                 "c3_1_1", "c3_1_2", "c3_1_3", "c3_1_4","c3_2_1", "c3_2_2",
                 "c3_2_3", "c3_2_4", "c3_3_1", "c3_3_2", "c3_3_3", "c3_4_1", "c3_4_2", "c3_4_3", "c3_4_4", "c3_4_5",
                 "c3_4_6", "c3_4_7", "c3_4_8", "c3_5_1", "c3_5_2", "c3_5_3", "c3_6_1", "c3_6_2", "c3_6_3", "c3_6_4",
                 "c3_7_1", "c3_7_2", "c3_7_3", "c4_1_1", "c4_1_2", "c4_1_2A", "c4_1_2B", "c4_1_2C", "c4_1_2D",
                 "c4_1_2E",
                 "c4_1_3", "c4_1_4", "c4_2_1", "c4_2_2", "c4_2_3", "c4_2_4", "c4_2_5", "c4_2_6", "c4_3_1", "c4_3_2",
                 "c4_3_3", "c4_3_4", "c4_4_1", "c4_4_2", "c5_1_1", "c5_1_2", "c5_1_3", "c5_1_3A", "c5_1_3B", "c5_1_3C",
                 "c5_1_3D", "c5_1_3E", "c5_1_3F", "c5_1_3G", "c5_1_3H", "c5_1_4", "c5_1_5", "c5_1_6", "c5_2_1",
                 "c5_2_2",
                 "c5_2_3", "c5_3_1", "c5_3_2", "c5_3_2A", "c5_3_2B", "c5_3_3", "c5_4_1A", "c5_4_1B", "c5_4_2", "c6_1_1",
                 "c6_1_2", "c6_2_1", "c6_2_2", "c6_2_3", "c6_2_4", "c6_3_1", "c6_3_2", "c6_3_3", "c6_3_4", "c6_3_5",
                 "c6_4_1", "c6_4_2", "c6_4_3", "c6_5_1", "c6_5_2", "c6_5_3", "c6_5_4", "c6_5_5", "c7_1_1",
                 "c7_1_2A", "c7_1_2B", "c7_1_2C", "c7_1_3", "c7_1_4", "c7_1_5", "c7_1_6", "c7_1_7A", "c7_1_7B",
                 "c7_1_7C",
                 "c7_1_7D", "c7_1_8", "c7_1_9", "c7_1_10", "c7_1_11", "c7_1_12", "c7_1_13", "c7_1_14", "c7_1_15",
                 "c7_1_16", "c7_1_17", "c7_1_18", "c7_1_19", "c7_2_1", "c7_3_1"]


# For Generating Data Tables for Excel CSV & PDF reports
def generate_reports():
    for cr_data in all_criterion:
        field_string = ""
        header_string = ""
        for key, value in all_field_values.items():
            if str(cr_data) == str(key):
                current_dict = all_field_values[key]
                for td_field in current_dict:
                    if td_field in ['file1', 'file2', 'file3', 'file4', 'file5']:
                        xtd = f"""<td> {{% if obj.file1 %}} {{{{obj.{td_field}.url}}}}
                             {{% else %}} No Files {{% endif %}} </td> """
                    else:
                        xtd = f""" <td> {{{{obj.{td_field} }}}} </td> """
                    field_string = field_string + xtd

                # # If current criterion Field key  matches with current loop from all criterion list
                for th_key in current_dict:
                    tr_field = current_dict[th_key]
                    xtr = f""" <th> {tr_field}  </th> """
                    header_string = header_string + xtr

        data_html = f""" 
                {{% extends 'criteria/reports/report_home.html' %}}
                {{% block table %}}
                
                <table id="example" class="display nowrap" style="width:100%">
                    <thead>
                        <tr>
                            <th> SL  </th>
                            {header_string}
                        </tr>
                
                    </thead>
                    <tbody>
                    {{% for obj in objects %}}
                        <tr>
                            <td> {{{{forloop.counter}}}} </td>
                             {field_string}
                        </tr>
                     {{% endfor %}}
                    </tbody>
                        <tfoot>
                            <tr>
                                 {header_string}
                            </tr>
                        </tfoot>
                    </table>
               {{% endblock %}}

        """

        filename = "templates/criteria/reports/" + str(cr_data) + ".html"
        fx = open(filename, "w")
        fx.write(data_html)
        fx.close()
    return "Table Report generated ..!"


# For Generating Criterion Data List & Approve Tables
def generate_tables():
    for cr_data in all_criterion:
        field_string = ""
        for key, value in all_field_values.items():

            if str(cr_data) == str(key):
                for td_field, th_field in value.items():
                    if td_field in ['file1', 'file2', 'file3', 'file4', 'file5']:
                        xtd = f"""
                              <tr>
                                <td> {th_field} </td>
                                <td> {{% if obj.{td_field} %}}
                                <a href="{{{{obj.{td_field}.url}}}}" target="_blank"> View </a>
                                 {{% else %}} No Files {{% endif %}} </td> 
                              </tr>   
                            """
                    else:
                        xtd = f""" 
                        <tr>
                            <td> {th_field} </td>
                            <td> {{{{obj.{td_field} }}}} </td> 
                        </tr>    
                        """
                    field_string = field_string + xtd
        data_html = f"""
                    {{% extends 'criteria/detailed_view.html' %}} {{% load static %}}
                    {{% block data_content %}}
            
                     {field_string}
                    
                   {{% endblock %}}
                    """
        filename = "templates/criteria/tables/" + str(cr_data) + ".html"
        fx = open(filename, "w")
        fx.write(data_html)
        fx.close()
    return "Table Report generated ..!"
