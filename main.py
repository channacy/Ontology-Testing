from owlready2 import *
import csv

omim_ontology_filepath = "data/omim_susc_import.owl"
do_ontology_filepath = "data/doid.owl"
subclasses = {}
is_a_classes = {}
subclasses_csv_file = "subclasses.csv"
is_a_csv_file = "is_a.csv"

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

    for cls in omin_onto.classes():
        classname_parts = str(cls).split(".")
        classname = classname_parts[1]
        for superclass in cls.is_a:
            superclass_name_parts = str(superclass).split(".")
            superclass_name = superclass_name_parts[1]
            if superclass_name in is_a_classes:
                is_a_classes[superclass_name].append(classname)
            else:
                is_a_classes[superclass_name] = [classname]

    print(is_a_classes)

    with open(subclasses_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, subclasses in subclasses_dict.items():
            writer.writerow([key, subclasses])

    with open(is_a_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, subclasses in is_a_classes.items():
            writer.writerow([key, subclasses])
        