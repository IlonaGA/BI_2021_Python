def check_gc_bounds(line, bottom, top):
    length = len(line)
    G_count = line.count('G')
    C_count = line.count('C')
    percent = ((G_count + C_count) / length) * 100

    if (percent < top) and (percent > bottom):
        return True
    else:
        return False


def check_length_bounds(line, bottom, top):
    length = len(line)
    if (length < top) and (length > bottom):
        return True
    else:
        return False


def check_quality_threshold(line, min_quality):
    summ = 0
    for char in line:
        summ += ord(char) - ord('!')
    return summ / len(line) > min_quality


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100),
         length_bounds=(0, 2**32), quality_threshold=0, save_filtered=False):
    if isinstance(gc_bounds, int) or isinstance(gc_bounds, float):
        gc_bounds = 0, gc_bounds

    if isinstance(length_bounds, int) or isinstance(length_bounds, float):
        length_bounds = 0, length_bounds

    fastq = open(input_fastq, 'r')
    passed = open(output_file_prefix + '_passed.fastq', 'w+')
    failed = open(output_file_prefix + '_failed.fastq', 'w+')
    file = []

    for line in fastq:
        file.append(line)

    for i in range(0, len(file), 4):
        if check_gc_bounds(file[i + 1],
                           gc_bounds[0],
                           gc_bounds[1]) and \
            check_length_bounds(file[i + 1],
                                length_bounds[0],
                                length_bounds[1]) and \
            check_quality_threshold(file[i + 1],
                                    quality_threshold):

            passed.write(file[i])
            passed.write(file[i + 1])
            passed.write(file[i + 2])
            passed.write(file[i + 3])

        elif save_filtered:
            failed.write(file[i])
            failed.write(file[i + 1])
            failed.write(file[i + 2])
            failed.write(file[i + 3])

    fastq.close()
    passed.close()
    failed.close()
