def test_save_reload_base_model(self):
    # Create a new object
    my_model = self.create_and_save_model()

    # Print the reloaded objects before saving
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    # Save the object
    my_model.save()

    # Print the reloaded objects after saving
    all_objs = storage.all()
    print("-- Reloaded objects after saving --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)
