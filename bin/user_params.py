 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='therapy_activation_time', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.therapy_activation_time = FloatText(
          value=10080,
          step=1000,
          style=style, layout=widget_layout)

        param_name2 = Button(description='number_of_injected_cells', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.number_of_injected_cells = IntText(
          value=500,
          step=10,
          style=style, layout=widget_layout)

        param_name3 = Button(description='worker_fraction', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.worker_fraction = FloatText(
          value=0.10,
          step=0.01,
          style=style, layout=widget_layout)

        param_name4 = Button(description='save_interval_after_therapy_start', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.save_interval_after_therapy_start = FloatText(
          value=60,
          step=1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='cargo_o2_relative_uptake', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.cargo_o2_relative_uptake = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name6 = Button(description='cargo_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.cargo_apoptosis_rate = FloatText(
          value=4.065e-5,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name7 = Button(description='cargo_relative_adhesion', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.cargo_relative_adhesion = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name8 = Button(description='cargo_relative_repulsion', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.cargo_relative_repulsion = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='worker_o2_relative_uptake', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.worker_o2_relative_uptake = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name10 = Button(description='worker_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.worker_apoptosis_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name11 = Button(description='worker_relative_adhesion', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.worker_relative_adhesion = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name12 = Button(description='worker_relative_repulsion', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.worker_relative_repulsion = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='worker_motility_persistence_time', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.worker_motility_persistence_time = FloatText(
          value=5.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='worker_migration_speed', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.worker_migration_speed = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='attached_worker_migration_bias', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.attached_worker_migration_bias = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='unattached_worker_migration_bias', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.unattached_worker_migration_bias = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='motility_shutdown_detection_threshold', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.motility_shutdown_detection_threshold = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name18 = Button(description='elastic_coefficient', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.elastic_coefficient = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name19 = Button(description='cargo_release_o2_threshold', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.cargo_release_o2_threshold = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='max_elastic_displacement', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.max_elastic_displacement = FloatText(
          value=50.0,
          step=1,
          style=style, layout=widget_layout)

        param_name21 = Button(description='damage_rate', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.damage_rate = FloatText(
          value=0.03333,
          step=0.01,
          style=style, layout=widget_layout)

        param_name22 = Button(description='repair_rate', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.repair_rate = FloatText(
          value=0.004167,
          step=0.001,
          style=style, layout=widget_layout)

        param_name23 = Button(description='drug_death_rate', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.drug_death_rate = FloatText(
          value=0.004167,
          step=0.001,
          style=style, layout=widget_layout)

        param_name24 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.tumor_radius = FloatText(
          value=200,
          step=10,
          style=style, layout=widget_layout)

        units_button1 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'

        desc_button1 = Button(description='time at which worker and cargo cells are injected', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='number of injected cells for therapy', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='fraction of injected cells that are workers', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='save (output) interval after therapy begins', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='cargo cell oxygen uptake rate (relative to cancer cells)', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='apoptosis rate for cargo cells', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='cargo cell adhesion (relative to cancer cells)', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='cargo cell repulsion (relative to cancer cells)', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='worker cell oxygen uptake rate (relative to cancer cells)', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='apoptosis rate for workers', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='worker cell adhesion (relative to cancer cells)', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='worker cell repulsion (relative to cancer cells)', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='motility persistence time for workers', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='migration speed for workers', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='migration bias for attached workers', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='migration bias for unattached workers', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='worker stops if chemoattractant < threshold', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='elastic coefficient for focal adhesion', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='oxygen threshold for releasing cargo', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='maximum distance to maintain focal adhesion', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='damage rate during therapy', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='repair rate during therapy', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='maximum drug-induced death rate', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='initial tumor radius', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'

        row1 = [param_name1, self.therapy_activation_time, units_button1, desc_button1] 
        row2 = [param_name2, self.number_of_injected_cells, units_button2, desc_button2] 
        row3 = [param_name3, self.worker_fraction, units_button3, desc_button3] 
        row4 = [param_name4, self.save_interval_after_therapy_start, units_button4, desc_button4] 
        row5 = [param_name5, self.cargo_o2_relative_uptake, units_button5, desc_button5] 
        row6 = [param_name6, self.cargo_apoptosis_rate, units_button6, desc_button6] 
        row7 = [param_name7, self.cargo_relative_adhesion, units_button7, desc_button7] 
        row8 = [param_name8, self.cargo_relative_repulsion, units_button8, desc_button8] 
        row9 = [param_name9, self.worker_o2_relative_uptake, units_button9, desc_button9] 
        row10 = [param_name10, self.worker_apoptosis_rate, units_button10, desc_button10] 
        row11 = [param_name11, self.worker_relative_adhesion, units_button11, desc_button11] 
        row12 = [param_name12, self.worker_relative_repulsion, units_button12, desc_button12] 
        row13 = [param_name13, self.worker_motility_persistence_time, units_button13, desc_button13] 
        row14 = [param_name14, self.worker_migration_speed, units_button14, desc_button14] 
        row15 = [param_name15, self.attached_worker_migration_bias, units_button15, desc_button15] 
        row16 = [param_name16, self.unattached_worker_migration_bias, units_button16, desc_button16] 
        row17 = [param_name17, self.motility_shutdown_detection_threshold, units_button17, desc_button17] 
        row18 = [param_name18, self.elastic_coefficient, units_button18, desc_button18] 
        row19 = [param_name19, self.cargo_release_o2_threshold, units_button19, desc_button19] 
        row20 = [param_name20, self.max_elastic_displacement, units_button20, desc_button20] 
        row21 = [param_name21, self.damage_rate, units_button21, desc_button21] 
        row22 = [param_name22, self.repair_rate, units_button22, desc_button22] 
        row23 = [param_name23, self.drug_death_rate, units_button23, desc_button23] 
        row24 = [param_name24, self.tumor_radius, units_button24, desc_button24] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.therapy_activation_time.value = float(uep.find('.//therapy_activation_time').text)
        self.number_of_injected_cells.value = int(uep.find('.//number_of_injected_cells').text)
        self.worker_fraction.value = float(uep.find('.//worker_fraction').text)
        self.save_interval_after_therapy_start.value = float(uep.find('.//save_interval_after_therapy_start').text)
        self.cargo_o2_relative_uptake.value = float(uep.find('.//cargo_o2_relative_uptake').text)
        self.cargo_apoptosis_rate.value = float(uep.find('.//cargo_apoptosis_rate').text)
        self.cargo_relative_adhesion.value = float(uep.find('.//cargo_relative_adhesion').text)
        self.cargo_relative_repulsion.value = float(uep.find('.//cargo_relative_repulsion').text)
        self.worker_o2_relative_uptake.value = float(uep.find('.//worker_o2_relative_uptake').text)
        self.worker_apoptosis_rate.value = float(uep.find('.//worker_apoptosis_rate').text)
        self.worker_relative_adhesion.value = float(uep.find('.//worker_relative_adhesion').text)
        self.worker_relative_repulsion.value = float(uep.find('.//worker_relative_repulsion').text)
        self.worker_motility_persistence_time.value = float(uep.find('.//worker_motility_persistence_time').text)
        self.worker_migration_speed.value = float(uep.find('.//worker_migration_speed').text)
        self.attached_worker_migration_bias.value = float(uep.find('.//attached_worker_migration_bias').text)
        self.unattached_worker_migration_bias.value = float(uep.find('.//unattached_worker_migration_bias').text)
        self.motility_shutdown_detection_threshold.value = float(uep.find('.//motility_shutdown_detection_threshold').text)
        self.elastic_coefficient.value = float(uep.find('.//elastic_coefficient').text)
        self.cargo_release_o2_threshold.value = float(uep.find('.//cargo_release_o2_threshold').text)
        self.max_elastic_displacement.value = float(uep.find('.//max_elastic_displacement').text)
        self.damage_rate.value = float(uep.find('.//damage_rate').text)
        self.repair_rate.value = float(uep.find('.//repair_rate').text)
        self.drug_death_rate.value = float(uep.find('.//drug_death_rate').text)
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//therapy_activation_time').text = str(self.therapy_activation_time.value)
        uep.find('.//number_of_injected_cells').text = str(self.number_of_injected_cells.value)
        uep.find('.//worker_fraction').text = str(self.worker_fraction.value)
        uep.find('.//save_interval_after_therapy_start').text = str(self.save_interval_after_therapy_start.value)
        uep.find('.//cargo_o2_relative_uptake').text = str(self.cargo_o2_relative_uptake.value)
        uep.find('.//cargo_apoptosis_rate').text = str(self.cargo_apoptosis_rate.value)
        uep.find('.//cargo_relative_adhesion').text = str(self.cargo_relative_adhesion.value)
        uep.find('.//cargo_relative_repulsion').text = str(self.cargo_relative_repulsion.value)
        uep.find('.//worker_o2_relative_uptake').text = str(self.worker_o2_relative_uptake.value)
        uep.find('.//worker_apoptosis_rate').text = str(self.worker_apoptosis_rate.value)
        uep.find('.//worker_relative_adhesion').text = str(self.worker_relative_adhesion.value)
        uep.find('.//worker_relative_repulsion').text = str(self.worker_relative_repulsion.value)
        uep.find('.//worker_motility_persistence_time').text = str(self.worker_motility_persistence_time.value)
        uep.find('.//worker_migration_speed').text = str(self.worker_migration_speed.value)
        uep.find('.//attached_worker_migration_bias').text = str(self.attached_worker_migration_bias.value)
        uep.find('.//unattached_worker_migration_bias').text = str(self.unattached_worker_migration_bias.value)
        uep.find('.//motility_shutdown_detection_threshold').text = str(self.motility_shutdown_detection_threshold.value)
        uep.find('.//elastic_coefficient').text = str(self.elastic_coefficient.value)
        uep.find('.//cargo_release_o2_threshold').text = str(self.cargo_release_o2_threshold.value)
        uep.find('.//max_elastic_displacement').text = str(self.max_elastic_displacement.value)
        uep.find('.//damage_rate').text = str(self.damage_rate.value)
        uep.find('.//repair_rate').text = str(self.repair_rate.value)
        uep.find('.//drug_death_rate').text = str(self.drug_death_rate.value)
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
