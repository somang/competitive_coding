




if __name__ == "__main__":
    fname = "input/e_also_big.in"
    f = open(fname)

    line = f.readline()
    while len(line.strip()) != 0:
        maximum_slices, num_types = line.split()
        #print("For Max {} slides, and {} pizza types.".format(maximum_slices, num_types))
        line = f.readline()
        pizza_types = line.split()
        #print("Slices {}.".format( pizza_types ))

        # Now, greedy algorithm, we take it from reverse order
        tmp_max = int(maximum_slices)
        pizza_index = int(num_types)
        ordering = ""
        counter = 0
        while pizza_types:
            cur_val = int(pizza_types.pop())
            pizza_index -= 1

            if tmp_max >= cur_val:
                tmp_max -= cur_val
                ordering = str(pizza_index) + " " + ordering
                counter += 1
        line = f.readline() # move to the next
    
        with open(fname.split(".")[0]+".out", "a") as outf:
            outf.write(str(counter))
            outf.write(ordering)
        
    f.close()
