from owlready2 import *
import csv

omim_ontology_filepath = "data/omim_susc_import.owl"
do_ontology_filepath = "data/doid.owl"
subclasses = {}
csv_file = "subclasses.csv"

if __name__=="__main__":
    subclasses_dict = {}
    omin_onto = get_ontology(omim_ontology_filepath).load()
    for cls in omin_onto.classes():
        classname = str(cls.name)
        if classname not in subclasses:
            subclasses_dict[classname] = []
        subclasses = cls.subclasses()
        if subclasses:
            # print(f"Subclasses of {cls.name}:")
            for subclass in subclasses:
                subclass_name = str(subclass.name)
                subclasses_dict[classname].append(subclass_name)
                # print(f"- {subclass.name}")
    #print(subclasses_dict)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, subclasses in subclasses_dict.items():
            writer.writerow([key, subclasses])
        