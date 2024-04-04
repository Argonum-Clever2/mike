import random

# Step 1: define the base
bases = ['A', 'T', 'G', 'C']

# Step 2: define genome length (in base pairs)
genome_length = 10000000

# genome_length = 10000000
# mutate_ratio = 4e-5  The mutation rate genome length is taken as the reciprocal divided by 40


# Step 3: Generation of ancestor haploid genome sequences
def generate_genome_sequence(genome_length):                                                                                                                                                     

    genome_sequences = []
    total_length = 0

    length = random.randint(0, genome_length//1000) 
    while total_length < genome_length:
        genome_sequences.append(''.join(random.choice(bases) for _ in range(length)))
        total_length += length
        length = random.randint(0, (genome_length-total_length))
    return genome_sequences



# haploid

def generate_genome_sequence(genome_length, count):
    genome_sequences = []
    for _ in range(count):
        genome_sequences.append(''.join(random.choice(bases) for i in range(genome_length)))
    return genome_sequences

# Step 4: generation of transposon sequences
transposon_length = 5000
transposon_percentage = 0.6
transposon_count = int(genome_length * transposon_percentage / transposon_length)

def generate_transposon_sequence(length):
    return ''.join(random.choice(bases) for _ in range(length))

transposon_sequences = []
transposon = generate_transposon_sequence(transposon_length)
for _ in range(transposon_count):
    transposon_sequences.append(transposon)

# generation of genome sequences
count = len(transposon_sequences)
genome_sequence = generate_genome_sequence(int(genome_length*(1-transposon_percentage)//count), count)

# random insertion of transposon sequences
genome_list = ""
if len(genome_sequence) > len(transposon_sequences):
    for _ in range(len(genome_sequence)):
        if _ >= len(transposon_sequences):
            genome_list += genome_sequence[_]
        else:
            genome_list += genome_sequence[_] + transposon_sequences[_]
else:
    for _ in range(len(transposon_sequences)):
        if _ >= len(genome_sequence):
            genome_list += transposon_sequences[_]
        else:
            genome_list += genome_sequence[_] + transposon_sequences[_]




# Step 5: mutation
mutation_rate = 4e-8
conserved_ratio = 0.8
conserved_bases = int(genome_length / 100) * 80

mutated_sequence = ''
for i, base in enumerate():
   if i % 100 == 0 and random.random() < mutation_rate:
       base = random.choice(bases)
   mutated_sequence += base

# Step 6: output as a FASTA file
output_filename = '/public/home/wangfang/simulate/simulate_a/genome_A_ancestor.fasta'

with open(output_filename, 'w') as output_file:
    output_file.write('>Ancestor\n')
    output_file.write(genome_list)

print(f"The simulation results have been saved to the file: {output_filename}")


# # same ploidy snp variation
def mutate_sequence(sequence, mutation_ratio, mutate_count, total_count):
    mutated_sequence = ""
    i = 0
    while i < len(sequence):
        if (i+1)%total_count == 0:
            for _ in range(mutate_count):
                if i < len(sequence):
                   if random.random() < mutation_ratio:
                       mutated_base = random.choice(bases)
                       mutated_sequence += mutated_base
                   else:
                       mutated_sequence += sequence[i]
                   i += 1
        
        else:
            mutated_sequence += sequence[i]
            i += 1
         
    return mutated_sequence


## autotetraploid
def mutate_sequence(sequence_arr, mutation_ratio, mutate_count, total_count):
    mutate_arr = []
    for line in range(len(sequence_arr)):
        mutate_arr.append("")
    i = 0
    while i < len(sequence_arr[0]):
        if (i+1)%total_count == 0:
            for _ in range(mutate_count):
                if i < len(sequence_arr[0]):
                    if random.random() < mutation_ratio:
                        mutated_base = random.choice(bases)
                        for ele in range(len(sequence_arr[0])):
                            mutate_arr[ele] += mutated_base
                    else:
                        for ele in range(len(sequence_arr[0])):
                            mutate_arr[ele] += sequence_arr[ele][i]
                    i += 1
        
        else:
            for ele in range(len(sequence_arr[0])):
                mutate_arr[ele] += sequence_arr[ele][i]
            i += 1
         
    return mutate_arr



# allotetraploid
def mutate_sequence(sequence_1, sequence_2, mutation_ratio, mutate_count, total_count):
    mutated_sequence_1 = ""
    mutated_sequence_2 = ""

    i = 0
    while i < len(sequence_1) and i < len(sequence_2):
        if (i+1)%total_count == 0:
            for _ in range(mutate_count):
                if i < len(sequence_1) and i < len(sequence_2):
                    if random.random() < mutation_ratio:
                        mutated_base = random.choice(bases)
                        mutated_sequence_1 += mutated_base
                    else:
                        mutated_sequence_1 += sequence_1[i]

                    if random.random() < mutation_ratio:
                        mutated_base = random.choice(bases)
                        mutated_sequence_2 += mutated_base
                    else:
                        mutated_sequence_2 += sequence_2[i]

                   i += 1
        
        else:
            mutated_sequence_1 += sequence_1[i]
            mutated_sequence_2 += sequence_2[i]
            i += 1
         
    return mutated_sequence_1, mutated_sequence_2

# Homologous identical ploidy simulation
# 模拟缺失（Deletion）
def simulate_deletion(sequence, start_position, deletion_length):
    return sequence[:start_position] + sequence[start_position+deletion_length:]


# 模拟插入（Insertion）
def simulate_insertion(sequence, insert_position, inserted_sequence):
    return sequence[:insert_position] + inserted_sequence + sequence[insert_position:]


# 模拟小片段倒位（Small Fragment Inversion）
def simulate_inversion(sequence, start_position, inversion_length):
    inverted_sequence = sequence[start_position:start_position+inversion_length][::-1]
    return sequence[:start_position] + inverted_sequence + sequence[start_position+inversion_length:]

# # 同源不同倍性模拟


# autotetraploid
def simulate_homo(sequence, mutate_ration, mutate_count, total_count, num_generations):
    sequence_list = []
    sequenceArr = []

    ratio = 0.002
    for _ in range(num_generations):
        mutated_sequence_1 = ""
        mutated_sequence_2 = ""
        mutated_sequence_3 = ""
        mutated_sequence_4 = ""

        

        i = 0
        while i < len(sequence):
            if (i+1)%total_count == 0:
                for _ in range(mutate_count):
                    if i < len(sequence):
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_1 += mutated_base
                        else:
                            mutated_sequence_1 += sequence[i]

                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_2 += mutated_base
                        else:
                            mutated_sequence_2 += sequence[i]
                        
                        if random.random() <  mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_3 += mutated_base
                        else:
                            mutated_sequence_3 += sequence[i]
                        
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_4 += mutated_base
                        else:
                            mutated_sequence_4 += sequence[i]
                        i += 1

            else:
                if (i < len(sequence)):
                    mutated_sequence_1 += sequence[i]
                    mutated_sequence_2 += sequence[i]
                    mutated_sequence_3 += sequence[i]
                    mutated_sequence_4 += sequence[i]
                    i += 1

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_1 = simulate_deletion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_1 = simulate_insertion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_1 = simulate_inversion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_2 = simulate_deletion(mutated_sequence_2, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_2 = simulate_insertion(mutated_sequence_2, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_2 = simulate_inversion(mutated_sequence_2, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  
        
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_3 = simulate_deletion(mutated_sequence_3, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_3 = simulate_insertion(mutated_sequence_3, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_3 = simulate_inversion(mutated_sequence_3, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_4 = simulate_deletion(mutated_sequence_4, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_4 = simulate_insertion(mutated_sequence_4, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_4 = simulate_inversion(mutated_sequence_4, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

        
         
        sequence_list.append(sequence)
        sequence_list.append(sequence)
        sequence_list.append(mutated_sequence_1)
        sequence_list.append(mutated_sequence_2)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()
        
        sequence_list.append(sequence)
        sequence_list.append(sequence)
        sequence_list.append(mutated_sequence_2)
        sequence_list.append(mutated_sequence_3)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()

        sequence_list.append(sequence)
        sequence_list.append(sequence)
        sequence_list.append(mutated_sequence_3)
        sequence_list.append(mutated_sequence_4)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()

        sequence_list.append(sequence)
        sequence_list.append(sequence)
        sequence_list.append(mutated_sequence_1)
        sequence_list.append(mutated_sequence_3)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()

    return sequenceArr


# diploid
def simulate_diplo(sequence, mutate_ration, mutate_count, total_count, num_generations):
    sequence_list = []
    sequenceArr = []

    ratio = 0.002
    for _ in range(num_generations):
        mutated_sequence_1 = ""
        mutated_sequence_2 = ""

        i = 0
        while i < len(sequence):
            if (i+1)%total_count == 0:
                for _ in range(mutate_count):
                    if i < len(sequence):
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_1 += mutated_base
                        else:
                            mutated_sequence_1 += sequence[i]

                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_2 += mutated_base
                        else:
                            mutated_sequence_2 += sequence[i]
                        

            else:
                if (i < len(sequence)):
                    mutated_sequence_1 += sequence[i]
                    mutated_sequence_2 += sequence[i]
                    i += 1

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_1 = simulate_deletion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_1 = simulate_insertion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_1 = simulate_inversion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_2 = simulate_deletion(mutated_sequence_2, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_2 = simulate_insertion(mutated_sequence_2, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_2 = simulate_inversion(mutated_sequence_2, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  
        
         
        sequence_list.append(sequence)
        sequence_list.append(mutated_sequence_1)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()
        
        sequence_list.append(sequence)
        sequence_list.append(mutated_sequence_2)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()
        
        sequence_list.append(mutated_sequence_1)
        sequence_list.append(mutated_sequence_2)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()

    return sequenceArr


# octoploid
def simulate_tooc(sequence_tetr, mutate_ration, mutate_count, total_count, num_generations):
    sequence_list = []
    sequenceArr = []

    ratio = 0.002
    for _ in range(num_generations):
        mutated_sequence_1 = ""
        mutated_sequence_2 = ""
        mutated_sequence_3 = ""
        mutated_sequence_4 = ""

        i = 0
        while i < len(sequence_tetr[0]):
            if (i+1)%total_count == 0:
                for _ in range(mutate_count):
                    if i < len(sequence_tetr[0]):
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_1 += mutated_base
                        else:
                            mutated_sequence_1 += sequence_tetr[0][i]

                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_2 += mutated_base
                        else:
                            mutated_sequence_2 += sequence_tetr[1][i]
                        
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_3 += mutated_base
                        else:
                            mutated_sequence_3 += sequence_tetr[2][i]
                            
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_4 += mutated_base
                        else:
                            mutated_sequence_4 += sequence_tetr[3][i]

            else:
                if (i < len(sequence_tetr[0])):
                    mutated_sequence_1 += sequence_tetr[0][i]
                    mutated_sequence_2 += sequence_tetr[1][i]
                    mutated_sequence_3 += sequence_tetr[2][i]
                    mutated_sequence_4 += sequence_tetr[3][i]
                    i += 1

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_1 = simulate_deletion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_1 = simulate_insertion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_1 = simulate_inversion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_2 = simulate_deletion(mutated_sequence_2, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_2 = simulate_insertion(mutated_sequence_2, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_2 = simulate_inversion(mutated_sequence_2, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_3 = simulate_deletion(mutated_sequence_3, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_3 = simulate_insertion(mutated_sequence_3, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_3 = simulate_inversion(mutated_sequence_3, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_4 = simulate_deletion(mutated_sequence_4, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_4 = simulate_insertion(mutated_sequence_4, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_4 = simulate_inversion(mutated_sequence_4, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)
            
        
        sequence_list.extend(sequence_tetr)
        sequence_list.append(mutated_sequence_1)
        sequence_list.append(mutated_sequence_2)
        sequence_list.append(mutated_sequence_3)
        sequence_list.append(mutated_sequence_4)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()
    return sequenceArr


# hexaploid
def simulate_hexa(sequence_tetr, sequence_tooc, mutate_ration, mutate_count, total_count, num_generations):
    sequence_list = []
    sequenceArr = []

    ratio = 0.002
    for _ in range(num_generations):
        mutated_sequence_1 = ""
        mutated_sequence_2 = ""
        mutated_sequence_3 = ""
        mutated_sequence_4 = ""
        mutated_sequence_5 = ""
        mutated_sequence_6 = ""

        i = 0
        while i < len(sequence_tetr[0]) and i < len(sequence_tooc[0]):
            if (i+1)%total_count == 0:
                for _ in range(mutate_count):
                    if i < len(sequence_tetr[0]) and i < len(sequence_tooc[0]):
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_1 += mutated_base
                        else:
                            mutated_sequence_1 += sequence_tetr[0][i]

                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_2 += mutated_base
                        else:
                            mutated_sequence_2 += sequence_tetr[1][i]
                        
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_3 += mutated_base
                        else:
                            mutated_sequence_3 += sequence_tooc[4][i]
                            
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_4 += mutated_base
                        else:
                            mutated_sequence_4 += sequence_tetr[5][i]
                        
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_5 += mutated_base
                        else:
                            mutated_sequence_5 += sequence_tetr[6][i]
                            
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_6 += mutated_base
                        else:
                            mutated_sequence_6 += sequence_tetr[7][i]
            else:
                if i < len(sequence_tetr[0]) and i < len(sequence_tooc[0]):
                    mutated_sequence_1 += sequence_tetr[0][i]
                    mutated_sequence_2 += sequence_tetr[1][i]
                    mutated_sequence_3 += sequence_tooc[4][i]
                    mutated_sequence_4 += sequence_tooc[5][i]
                    mutated_sequence_5 += sequence_tooc[6][i]
                    mutated_sequence_6 += sequence_tooc[7][i]
                    i += 1

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_1 = simulate_deletion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_1 = simulate_insertion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_1 = simulate_inversion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_2 = simulate_deletion(mutated_sequence_2, random.randint(0, len(mutated_sequence_2)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_2 = simulate_insertion(mutated_sequence_2, random.randint(0, len(mutated_sequence_2)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_2 = simulate_inversion(mutated_sequence_2, random.randint(0, len(mutated_sequence_2)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_3 = simulate_deletion(mutated_sequence_3, random.randint(0, len(mutated_sequence_3)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_3 = simulate_insertion(mutated_sequence_3, random.randint(0, len(mutated_sequence_3)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_3 = simulate_inversion(mutated_sequence_3, random.randint(0, len(mutated_sequence_3)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_4 = simulate_deletion(mutated_sequence_4, random.randint(0, len(mutated_sequence_4)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_4 = simulate_insertion(mutated_sequence_4, random.randint(0, len(mutated_sequence_4)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_4 = simulate_inversion(mutated_sequence_4, random.randint(0, len(mutated_sequence_4)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_5 = simulate_deletion(mutated_sequence_5, random.randint(0, len(mutated_sequence_4)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_5 = simulate_insertion(mutated_sequence_5, random.randint(0, len(mutated_sequence_5)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_5 = simulate_inversion(mutated_sequence_5, random.randint(0, len(mutated_sequence_5)-inversion_length-1), inversion_length)
        
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_6 = simulate_deletion(mutated_sequence_6, random.randint(0, len(mutated_sequence_6)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_6 = simulate_insertion(mutated_sequence_6, random.randint(0, len(mutated_sequence_6)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_6 = simulate_inversion(mutated_sequence_6, random.randint(0, len(mutated_sequence_6)-inversion_length-1), inversion_length)
            

        sequence_list.append(mutated_sequence_1)
        sequence_list.append(mutated_sequence_2)
        sequence_list.append(mutated_sequence_3)
        sequence_list.append(mutated_sequence_4)
        sequence_list.append(mutated_sequence_5)
        sequence_list.append(mutated_sequence_6)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()
    return sequenceArr

# 12-ploid
def simulate_12(sequence_tetr, mutate_ration, mutate_count, total_count, num_generations):
    sequence_list = []
    sequenceArr = []

    ratio = 0.002
    for _ in range(num_generations):
        mutated_sequence_1 = ""
        mutated_sequence_2 = ""
        mutated_sequence_3 = ""
        mutated_sequence_4 = ""
        mutated_sequence_5 = ""
        mutated_sequence_6 = ""

        i = 0
        while i < len(sequence_tetr[0]) :
            if (i+1)%total_count == 0:
                for _ in range(mutate_count):
                    if i < len(sequence_tetr[0]) :
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_1 += mutated_base
                        else:
                            mutated_sequence_1 += sequence_tetr[0][i]

                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_2 += mutated_base
                        else:
                            mutated_sequence_2 += sequence_tetr[1][i]
                        
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_3 += mutated_base
                        else:
                            mutated_sequence_3 += sequence_tetr[2][i]
                            
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_4 += mutated_base
                        else:
                            mutated_sequence_4 += sequence_tetr[3][i]
                        
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_5 += mutated_base
                        else:
                            mutated_sequence_5 += sequence_tetr[4][i]
                            
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_6 += mutated_base
                        else:
                            mutated_sequence_6 += sequence_tetr[5][i]
            else:
                if i < len(sequence_tetr[0]) :
                    mutated_sequence_1 += sequence_tetr[0][i]
                    mutated_sequence_2 += sequence_tetr[1][i]
                    mutated_sequence_3 += sequence_tetr[2][i]
                    mutated_sequence_4 += sequence_tetr[3][i]
                    mutated_sequence_5 += sequence_tetr[4][i]
                    mutated_sequence_6 += sequence_tetr[5][i]
                    i += 1

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_1 = simulate_deletion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_1 = simulate_insertion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_1 = simulate_inversion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_2 = simulate_deletion(mutated_sequence_2, random.randint(0, len(mutated_sequence_2)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_2 = simulate_insertion(mutated_sequence_2, random.randint(0, len(mutated_sequence_2)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_2 = simulate_inversion(mutated_sequence_2, random.randint(0, len(mutated_sequence_2)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_3 = simulate_deletion(mutated_sequence_3, random.randint(0, len(mutated_sequence_3)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_3 = simulate_insertion(mutated_sequence_3, random.randint(0, len(mutated_sequence_3)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_3 = simulate_inversion(mutated_sequence_3, random.randint(0, len(mutated_sequence_3)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_4 = simulate_deletion(mutated_sequence_4, random.randint(0, len(mutated_sequence_4)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_4 = simulate_insertion(mutated_sequence_4, random.randint(0, len(mutated_sequence_4)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_4 = simulate_inversion(mutated_sequence_4, random.randint(0, len(mutated_sequence_4)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_5 = simulate_deletion(mutated_sequence_5, random.randint(0, len(mutated_sequence_4)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_5 = simulate_insertion(mutated_sequence_5, random.randint(0, len(mutated_sequence_5)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_5 = simulate_inversion(mutated_sequence_5, random.randint(0, len(mutated_sequence_5)-inversion_length-1), inversion_length)
        
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_6 = simulate_deletion(mutated_sequence_6, random.randint(0, len(mutated_sequence_6)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_6 = simulate_insertion(mutated_sequence_6, random.randint(0, len(mutated_sequence_6)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_6 = simulate_inversion(mutated_sequence_6, random.randint(0, len(mutated_sequence_6)-inversion_length-1), inversion_length)
            

        sequence_list.extend(sequence_tetr)
        sequence_list.append(mutated_sequence_1)
        sequence_list.append(mutated_sequence_2)
        sequence_list.append(mutated_sequence_3)
        sequence_list.append(mutated_sequence_4)
        sequence_list.append(mutated_sequence_5)
        sequence_list.append(mutated_sequence_6)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()
    return sequenceArr



# 16-ploid
def simulate_16(sequence_tooc, mutate_ration, mutate_count, total_count, num_generations):
    sequence_list = []
    sequenceArr = []

    ratio = 0.002
    for _ in range(num_generations):
        mutated_sequence_1 = ""
        mutated_sequence_2 = ""
        mutated_sequence_3 = ""
        mutated_sequence_4 = ""
        mutated_sequence_5 = ""
        mutated_sequence_6 = ""
        mutated_sequence_7 = ""
        mutated_sequence_8 = ""

        i = 0
        while i < len(sequence_tooc[0]) :
            if (i+1)%total_count == 0:
                for _ in range(mutate_count):
                    if i < len(sequence_tooc[0]) :
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_1 += mutated_base
                        else:
                            mutated_sequence_1 += sequence_tooc[0][i]

                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_2 += mutated_base
                        else:
                            mutated_sequence_2 += sequence_tooc[1][i]
                        
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_3 += mutated_base
                        else:
                            mutated_sequence_3 += sequence_tooc[2][i]
                            
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_4 += mutated_base
                        else:
                            mutated_sequence_4 += sequence_tooc[3][i]
                        
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_5 += mutated_base
                        else:
                            mutated_sequence_5 += sequence_tooc[4][i]
                            
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_6 += mutated_base
                        else:
                            mutated_sequence_6 += sequence_tooc[5][i]
                        
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_7 += mutated_base
                        else:
                            mutated_sequence_7 += sequence_tooc[6][i]
                            
                        if random.random() < mutate_ration:
                            mutated_base = random.choice(bases)
                            mutated_sequence_8 += mutated_base
                        else:
                            mutated_sequence_8 += sequence_tooc[7][i]
                            
            else:
                if i < len(sequence_tooc[0]) :
                    mutated_sequence_1 += sequence_tooc[0][i]
                    mutated_sequence_2 += sequence_tooc[1][i]
                    mutated_sequence_3 += sequence_tooc[2][i]
                    mutated_sequence_4 += sequence_tooc[3][i]
                    mutated_sequence_5 += sequence_tooc[4][i]
                    mutated_sequence_6 += sequence_tooc[5][i]
                    mutated_sequence_7 += sequence_tooc[6][i]
                    mutated_sequence_8 += sequence_tooc[7][i]
                    i += 1

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_1 = simulate_deletion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_1 = simulate_insertion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_1 = simulate_inversion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_2 = simulate_deletion(mutated_sequence_2, random.randint(0, len(mutated_sequence_2)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_2 = simulate_insertion(mutated_sequence_2, random.randint(0, len(mutated_sequence_2)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_2 = simulate_inversion(mutated_sequence_2, random.randint(0, len(mutated_sequence_2)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_3 = simulate_deletion(mutated_sequence_3, random.randint(0, len(mutated_sequence_3)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_3 = simulate_insertion(mutated_sequence_3, random.randint(0, len(mutated_sequence_3)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_3 = simulate_inversion(mutated_sequence_3, random.randint(0, len(mutated_sequence_3)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_4 = simulate_deletion(mutated_sequence_4, random.randint(0, len(mutated_sequence_4)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_4 = simulate_insertion(mutated_sequence_4, random.randint(0, len(mutated_sequence_4)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_4 = simulate_inversion(mutated_sequence_4, random.randint(0, len(mutated_sequence_4)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_5 = simulate_deletion(mutated_sequence_5, random.randint(0, len(mutated_sequence_4)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_5 = simulate_insertion(mutated_sequence_5, random.randint(0, len(mutated_sequence_5)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_5 = simulate_inversion(mutated_sequence_5, random.randint(0, len(mutated_sequence_5)-inversion_length-1), inversion_length)
        
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_6 = simulate_deletion(mutated_sequence_6, random.randint(0, len(mutated_sequence_6)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_6 = simulate_insertion(mutated_sequence_6, random.randint(0, len(mutated_sequence_6)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_6 = simulate_inversion(mutated_sequence_6, random.randint(0, len(mutated_sequence_6)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_7 = simulate_deletion(mutated_sequence_7, random.randint(0, len(mutated_sequence_7)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_7 = simulate_insertion(mutated_sequence_7, random.randint(0, len(mutated_sequence_7)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_7 = simulate_inversion(mutated_sequence_7, random.randint(0, len(mutated_sequence_7)-inversion_length-1), inversion_length)
            
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_8 = simulate_deletion(mutated_sequence_8, random.randint(0, len(mutated_sequence_8)-deletion_length-1), deletion_length)            
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_8 = simulate_insertion(mutated_sequence_8, random.randint(0, len(mutated_sequence_8)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_8 = simulate_inversion(mutated_sequence_8, random.randint(0, len(mutated_sequence_8)-inversion_length-1), inversion_length)
            

        sequence_list.extend(sequence_tooc)
        sequence_list.append(mutated_sequence_1)
        sequence_list.append(mutated_sequence_2)
        sequence_list.append(mutated_sequence_3)
        sequence_list.append(mutated_sequence_4)
        sequence_list.append(mutated_sequence_5)
        sequence_list.append(mutated_sequence_6)
        sequence_list.append(mutated_sequence_7)
        sequence_list.append(mutated_sequence_8)
        sequenceArr.append(sequence_list.copy())
        sequence_list.clear()
    return sequenceArr




# autotetraploid
ancestorArr = []
ancestorArr.append(genome_list.copy())
ancestorArr.append(genome_list.copy())
ancestorArr.append(genome_list.copy())
ancestorArr.append(genome_list.copy())

# allotetraploid
ancestorArr = []
ancestorArr.append(genome_list)
ancestorArr.append(genome_list)
ancestorArr.append(genome_list_other)
ancestorArr.append(genome_list_other)


mutate_ration = 0.002
mutate_count = 20
total_count = 100
num_generations = 1
# ancestor diploid
sequence_diplo_arr = simulate_diplo(genome_list, mutate_ration, mutate_count, total_count, num_generations)

# ancestor tetraploid
sequence_tetr_arr = simulate_homo(genome_list, mutate_ration, mutate_count, total_count, num_generations)

# octoploid
sequence_tooc_arr = simulate_tooc(sequence_tetr_arr, mutate_ration, mutate_count, total_count, num_generations)

# hexaploid
sequence_hexa_arr = simulate_hexa(sequence_tetr_arr, sequence_tooc_arr, mutate_ration, mutate_count, total_count, num_generations)

# 12-ploid
sequence_12_arr = simulate_12(sequence_hexa_arr, mutate_ration, mutate_count, total_count, num_generations)

# 16-ploid
sequence_16_arr = simulate_16(sequence_tooc_arr, mutate_ration, mutate_count, total_count, num_generations)


# 祖先序列写入文件(ancestor genome to file)
def save_file(sequence_diplo_arr, sequence_tetr_arr, sequence_tooc_arr, sequence_hexa_arr, sequence_12_arr, sequence_16_arr, name):
    for i in range(len(sequence_diplo_arr)):
        output_filename = '/public/home/wangfang/simulate/mono_d/{}Diplo{}.fasta'.format(name, i)
        with open(output_filename, "w") as fp:
            for _ in range(len(sequence_diplo_arr[i])):
                fp.write(">{}Diplot_0{}\n".format(name, _))
                fp.write("{}\n".format(sequence_diplo_arr[i][_]))


    for i in range(len(sequence_tetr_arr)):
        output_filename = '/public/home/wangfang/simulate/mono_d/{}Tetr{}.fasta'.format(name, i)
        with open(output_filename, "w") as fp:
            for _ in range(len(sequence_diplo_arr[i])):
                fp.write(">{}Tetr_0{}\n".format(name, _))
                fp.write("{}\n".format(sequence_diplo_arr[i][_]))
                


    for i in range(len(sequence_tooc_arr)):
        output_filename = '/public/home/wangfang/simulate/mono_d/{}Tooc{}.fasta'.format(name, i)
        with open(output_filename, "w") as fp:
            for _ in range(len(sequence_diplo_arr[i])):
                fp.write(">{}Tooc_0{}\n".format(name, _))
                fp.write("{}\n".format(sequence_diplo_arr[i][_]))
                

    for i in range(len(sequence_hexa_arr)):
        output_filename = '/public/home/wangfang/simulate/mono_d/{}Hexa{}.fasta'.format(name, i)
        with open(output_filename, "w") as fp:
            for _ in range(len(sequence_diplo_arr[i])):
                fp.write(">{}Hexa_0{}\n".format(name, _))
                fp.write("{}\n".format(sequence_diplo_arr[i][_]))
                

    for i in range(len(sequence_12_arr)):
        output_filename = '/public/home/wangfang/simulate/mono_d/{}12{}.fasta'.format(name, i)
        with open(output_filename, "w") as fp:
            for _ in range(len(sequence_diplo_arr[i])):
                fp.write(">{}12_0{}\n".format(name, _))
                fp.write("{}\n".format(sequence_diplo_arr[i][_]))
            

    for i in range(len(sequence_16_arr)):
        output_filename = '/public/home/wangfang/simulate/mono_d/{}16{}.fasta'.format(name, i)
        with open(output_filename, "w") as fp:
            for _ in range(len(sequence_diplo_arr[i])):
                fp.write(">{}16_0{}\n".format(name, _))
                fp.write("{}\n".format(sequence_diplo_arr[i][_]))
            

name = "ancestor"    
save_file(sequence_diplo_arr, sequence_tetr_arr, sequence_tooc_arr, sequence_hexa_arr, sequence_12_arr, sequence_16_arr, name)
       

# 同源倍性相同数据模拟(Simulation of autotetraploid)

def evolve_sequence(ancestor_sequence, mutation_rate, num_generations):
    ratio = 4e-7
    mutated_sequence_1 = ancestor_sequence
    mutate_count = 20
    total_count = 100
    for generation in range(num_generations):
        mutated_sequence_1 = mutate_sequence(mutated_sequence_1, mutation_rate, mutate_count, total_count)
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            mutated_sequence_1 = simulate_deletion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            mutated_sequence_1 = simulate_insertion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            mutated_sequence_1 = simulate_inversion(mutated_sequence_1, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

    return mutated_sequence_1


# 同源不同倍性数据模拟 (Simulation of allotetraploid)
def evolve_sequence(ancestor_sequence_arr, mutation_rate, num_generations):
    ratio = 4e-7
    mutate_count = 20
    total_count = 100
    mutated_sequence_arr = ancestor_sequence_arr
    for generation in range(num_generations):
        mutated_sequence_arr = mutate_sequence(mutated_sequence_arr, mutation_rate, mutate_count, total_count)
        for ele in range(len(mutated_sequence_arr)):
            if random.random() < ratio:
                deletion_length = random.randint(2, 10)
                mutated_sequence_arr[ele] = simulate_deletion(mutated_sequence_arr[ele], random.randint(0, len(mutated_sequence_arr[ele])-deletion_length-1), deletion_length)
            if random.random() < ratio:
                insertion_length = random.randint(2, 10)
                insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
                mutated_sequence_arr[ele] = simulate_insertion(mutated_sequence_arr[ele], random.randint(0, len(mutated_sequence_arr[ele])-1), insertion_sequence)    
            if random.random() < ratio:
                inversion_length = random.randint(200, 1000)
                mutated_sequence_arr[ele] = simulate_inversion(mutated_sequence_arr[ele], random.randint(0, len(mutated_sequence_arr[ele])-inversion_length-1), inversion_length)  

    return mutated_sequence_arr

# 异源四倍体(allotetraploid)

def evolve_sequence(ancestor_sequence, ancestor_sequence_other, mutation_rate, num_generations):
    ratio = 4e-7
    current_sequence_1 = ancestor_sequence
    current_sequence_2 = ancestor_sequence_other
    mutate_count = 20
    total_count = 100
    for generation in range(num_generations):
        current_sequence_1, current_sequence_2 = mutate_sequence(current_sequence_1, current_sequence_2, mutation_rate, mutate_count, total_count)
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            current_sequence_1 = simulate_deletion(current_sequence_1, random.randint(0, len(current_sequence_1)-deletion_length-1), deletion_length)
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            current_sequence_1 = simulate_insertion(current_sequence_1, random.randint(0, len(current_sequence_1)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            current_sequence_1 = simulate_inversion(current_sequence_1, random.randint(0, len(current_sequence_1)-inversion_length-1), inversion_length)
        
        if random.random() < ratio:
            deletion_length = random.randint(2, 10)
            current_sequence_2 = simulate_deletion(current_sequence_2, random.randint(0, len(current_sequence_2)-deletion_length-1), deletion_length)
        if random.random() < ratio:
            insertion_length = random.randint(2, 10)
            insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
            current_sequence_2 = simulate_insertion(current_sequence_2, random.randint(0, len(current_sequence_2)-1), insertion_sequence)    
        if random.random() < ratio:
            inversion_length = random.randint(200, 1000)
            current_sequence_2 = simulate_inversion(current_sequence_2, random.randint(0, len(current_sequence_2)-inversion_length-1), inversion_length) 


    return current_sequence_1, current_sequence_2




# # 单倍体 (haploid)
# def get_offsprings(sequence, mutation_ration, num_offsprings):
#     mutated_sequence_1 = []
#     mutate_count = 20
#     total_count = 100
#     for num_offsprings in range(num_offsprings):
#         mutated_sequence_1.append(mutate_sequence(sequence, mutation_rate, mutate_count, total_count))
#     return mutated_sequence_1

# 异源四倍体 (allotetraploid)

# def simulate_allo(sequence_1, sequence_2, mutate_ration, mutate_count, total_count, num_generations):
#     sequence_list = []
#     sequenceArr = []

#     ratio = 0.002
#     for _ in range(num_generations):
#         mutated_sequence_11 = ""
#         mutated_sequence_12 = ""
#         mutated_sequence_21 = ""
#         mutated_sequence_22 = ""

        

#         i = 0
#         while i < len(sequence_1) and i < len (sequence_2):
#             if (i+1)%total_count == 0:
#                 for _ in range(mutate_count):
#                     if i < len(sequence_1) and i < len(sequence_2):
#                         if random.random() < mutate_ration:
#                             mutated_base = random.choice(bases)
#                             mutated_sequence_11 += mutated_base
#                         else:
#                             mutated_sequence_11 += sequence_1[i]

#                         if random.random() < mutate_ration:
#                             mutated_base = random.choice(bases)
#                             mutated_sequence_12 += mutated_base
#                         else:
#                             mutated_sequence_12 += sequence_1[i]
                        
#                         if random.random() <  mutate_ration:
#                             mutated_base = random.choice(bases)
#                             mutated_sequence_21 += mutated_base
#                         else:
#                             mutated_sequence_21 += sequence_2[i]
                        
#                         if random.random() < mutate_ration:
#                             mutated_base = random.choice(bases)
#                             mutated_sequence_22 += mutated_base
#                         else:
#                             mutated_sequence_22 += sequence_2[i]
#                         i += 1

#             else:
#                 if i < len(sequence_1) and i < len(sequence_2):
#                     mutated_sequence_11 += sequence_1[i]
#                     mutated_sequence_12 += sequence_1[i]
#                     mutated_sequence_21 += sequence_2[i]
#                     mutated_sequence_22 += sequence_2[i]
#                     i += 1

#         if random.random() < ratio:
#             deletion_length = random.randint(2, 10)
#             mutated_sequence_11 = simulate_deletion(mutated_sequence_11, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
#         if random.random() < ratio:
#             insertion_length = random.randint(2, 10)
#             insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
#             mutated_sequence_11 = simulate_insertion(mutated_sequence_11, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
#         if random.random() < ratio:
#             inversion_length = random.randint(200, 1000)
#             mutated_sequence_11 = simulate_inversion(mutated_sequence_11, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

#         if random.random() < ratio:
#             deletion_length = random.randint(2, 10)
#             mutated_sequence_12 = simulate_deletion(mutated_sequence_12, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
#         if random.random() < ratio:
#             insertion_length = random.randint(2, 10)
#             insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
#             mutated_sequence_12 = simulate_insertion(mutated_sequence_12, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
#         if random.random() < ratio:
#             inversion_length = random.randint(200, 1000)
#             mutated_sequence_12 = simulate_inversion(mutated_sequence_12, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  
        
#         if random.random() < ratio:
#             deletion_length = random.randint(2, 10)
#             mutated_sequence_21 = simulate_deletion(mutated_sequence_21, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
#         if random.random() < ratio:
#             insertion_length = random.randint(2, 10)
#             insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
#             mutated_sequence_21 = simulate_insertion(mutated_sequence_21, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
#         if random.random() < ratio:
#             inversion_length = random.randint(200, 1000)
#             mutated_sequence_21 = simulate_inversion(mutated_sequence_21, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

#         if random.random() < ratio:
#             deletion_length = random.randint(2, 10)
#             mutated_sequence_22 = simulate_deletion(mutated_sequence_22, random.randint(0, len(mutated_sequence_1)-deletion_length-1), deletion_length)            
#         if random.random() < ratio:
#             insertion_length = random.randint(2, 10)
#             insertion_sequence = ''.join(random.choice(bases) for _ in range(insertion_length))
#             mutated_sequence_22 = simulate_insertion(mutated_sequence_22, random.randint(0, len(mutated_sequence_1)-1), insertion_sequence)    
#         if random.random() < ratio:
#             inversion_length = random.randint(200, 1000)
#             mutated_sequence_22 = simulate_inversion(mutated_sequence_22, random.randint(0, len(mutated_sequence_1)-inversion_length-1), inversion_length)  

        
         
#         sequence_list.append(sequence_1)
#         sequence_list.append(sequence_2)
#         sequence_list.append(mutated_sequence_11)
#         sequence_list.append(mutated_sequence_21)

#         sequenceArr.append(sequence_list.copy())
#         sequence_list.clear()
        
#         sequence_list.append(sequence_1)
#         sequence_list.append(sequence_2)
#         sequence_list.append(mutated_sequence_11)
#         sequence_list.append(mutated_sequence_22)
#         sequenceArr.append(sequence_list.copy())
#         sequence_list.clear()

#         sequence_list.append(sequence_1)
#         sequence_list.append(sequence_2)
#         sequence_list.append(mutated_sequence_12)
#         sequence_list.append(mutated_sequence_21)
#         sequenceArr.append(sequence_list.copy())
#         sequence_list.clear()

#         sequence_list.append(sequence_1)
#         sequence_list.append(sequence_2)
#         sequence_list.append(mutated_sequence_12)
#         sequence_list.append(mutated_sequence_22)
#         sequenceArr.append(sequence_list.copy())
#         sequence_list.clear()

#     return sequenceArr


# 模拟异源四倍体 (Simulation of allotetraploid)
# mutate_count = 20
# total_count = 100
# mutation_rate = 4e-7
# num_generations = 100
# offspring_1, offspring_2 = evolve_sequence(genome_list, genome_list_other, mutation_rate, num_generations)
# num_offsprings = 4
# generation = 1
# offsprings = simulate_allo(offspring_1, offspring_2, mutation_rate, mutate_count, total_count, generation)
# for i in range(len(offsprings)):
#     filename = "/public/home/wangfang/simulate/mono_b/B00{}.fasta".format(i)
#     with open(filename, "w") as fp:
#         for _ in range(len(offsprings[i])):
#             fp.write(">A00{}{}\n".format(i, _))
#             fp.write("{}\n".format(offsprings[i][_]))

# for fileSuf in range(1, 10):
#     num_generations = 100
#     offspring_1, offspring_2 = evolve_sequence(offsprings[0][0], offsprings[0][1], mutation_rate, num_generations)
#     offsprings = simulate_allo(offspring_1, offspring_2, mutation_rate, mutate_count, total_count, generation)
#     for i in range(len(offsprings)):
#         filename = "/public/home/wangfang/simulate/mono_b/B00{}.fasta".format(i+4*fileSuf)
#         with open(filename, "w") as fp:
#             for _ in range(len(offsprings[i])):
#                 fp.write(">B00{}{}\n".format(i, _))
#                 fp.write("{}\n".format(offsprings[i][_]))


# for _ in range(10, 13):
#     num_generations = 1000
#     offspring_1, offspring_2 = evolve_sequence(offsprings[0][0], offsprings[0][1], mutation_rate, num_generations)
#     offsprings = simulate_homo(offspring, mutation_rate, mutate_count, total_count, generation)
#     for i in range(len(offsprings)):
#         filename = "/public/home/wangfang/simulate/mono_b/B00{}.fasta".format(i+4*fileSuf)
#         with open(filename, "w") as fp:
#             for _ in range(len(offsprings[i])):
#                 fp.write(">B00{}{}\n".format(i, _))
#                 fp.write("{}\n".format(offsprings[i][_]))



# 模拟同源四倍体 (Simulation of autotetraploid)
# mutate_count = 20
# total_count = 100
# mutation_rate = 4e-7
# num_generations = 100
# offspring = evolve_sequence(genome_list, mutation_rate, num_generations)
# num_offsprings = 4
# generation = 1
# offsprings = simulate_homo(offspring, mutation_rate, mutate_count, total_count, generation)
# for i in range(len(offsprings)):
#     filename = "/public/home/wangfang/simulate/mono_a/A00{}.fasta".format(i)
#     with open(filename, "w") as fp:
#         for _ in range(len(offsprings[i])):
#             fp.write(">A00{}{}\n".format(i, _))
#             fp.write("{}\n".format(offsprings[i][_]))

# for fileSuf in range(1, 10):
#     num_generations = 100
#     offspring = evolve_sequence(offsprings[0][0], mutation_rate, num_generations)
#     offsprings = simulate_homo(offspring, mutation_rate, mutate_count, total_count, generation)
#     for i in range(len(offsprings)):
#         filename = "/public/home/wangfang/simulate/mono_a/A00{}.fasta".format(i+4*fileSuf)
#         with open(filename, "w") as fp:
#             for _ in range(len(offsprings[i])):
#                 fp.write(">A00{}{}\n".format(i, _))
#                 fp.write("{}\n".format(offsprings[i][_]))


# for _ in range(10, 13):
#     num_generations = 1000
#     offspring = evolve_sequence(offsprings[0][0], mutation_rate, num_generations)
#     offsprings = simulate_homo(offspring, mutation_rate, mutate_count, total_count, generation)
#     for i in range(len(offsprings)):
#         filename = "/public/home/wangfang/simulate/mono_a/A00{}.fasta".format(i+4*fileSuf)
#         with open(filename, "w") as fp:
#             for _ in range(len(offsprings[i])):
#                 fp.write(">A00{}{}\n".format(i, _))
#                 fp.write("{}\n".format(offsprings[i][_]))


# Simulation of ploid
mutate_count = 20
total_count = 100
mutation_rate = 4e-7
num_generations = 100
mutate_ration = 4e-7
num_offsprings = 1
# 二倍体进化 (the simulation of evolution)
offsprings_diplo = evolve_sequence(genome_list, mutation_rate, num_generations)
# 四倍体进化 (the simulation of evolution)
offsprings_tetr = evolve_sequence(sequence_tetr_arr[0][1], mutation_rate, num_generations)
tetr_arr = simulate_homo(offsprings_tetr, mutate_ration, mutate_count, total_count, num_offsprings)
# 八倍体进化 (the simulation of evolution)
offsprings_tooc = evolve_sequence(sequence_tooc_arr[0][1], mutation_rate, num_generations)
# 六倍体 (the simulation of evolution)
offsprings_hexa = evolve_sequence(sequence_hexa_arr[0][1], mutation_rate, num_generations)
#12倍体 (the simulation of evolution)
offsprings_12 = evolve_sequence(sequence_12_arr[0][1], mutation_rate, num_generations)
# 16倍体 (the simulation of evolution)
offsprings_16 = evolve_sequence(sequence_16_arr[0][1], mutation_rate, num_generations)








# 模拟单倍体
# num_generations = 100
# offspring = evolve_sequence(offsprings[0], mutation_rate, num_generations)
# mutation_rate = 4e-7
# num_offsprings = 4
# offsprings = get_offsprings(offspring, mutation_rate, num_offsprings)

# for i in range(len(offsprings)):
#     filename="./A00{}.fasta".format(i+4*6)
#     with open(filename, "w") as fp:
#         fp.write(">A00{}\n".format(i+4*6))
#         fp.write(offsprings[i])
