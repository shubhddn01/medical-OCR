from parser_generic import MedicalDocParser
import re

class PresciptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self,text)

    
    def parse(self):
        return {
            'patient_name':self.get_field('patient_name'),
            'address':self.get_field('address'),
            'medicines':self.get_field('medicines'),
            'directions':self.get_field('directions'),
            'refill':self.get_field('refill'),
        }
    
    def get_field(self,field_name):
        pattern_dic={
            'patient_name':{'pattern':'Name:(.*)Date', 'flag':0},
            'address':{'pattern':'Address:(.*)\n','flag': 0},
            'medicines':{'pattern':'Address[^\n]*(.*)Directions','flag':re.DOTALL},
            'directions':{'pattern': 'Directions:(.*)Refill','flag':re.DOTALL},
            'refill':{'pattern':'Refill:(.*)times','flag':0}
        }

        pattern_object = pattern_dic.get(field_name)
        if pattern_object:
            matches =  re.findall(pattern_object['pattern'],self.text,flags=pattern_object['flag'])
            if(len(matches)>0):
                return matches[0].strip()


if __name__ == '__main__':
    PresciptionParser('abc')


