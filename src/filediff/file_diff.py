import click

@click.command()
@click.option('-f1', '--file1', required=True)
@click.option('-f2', '--file2', required=True)
@click.option('-o', '--output', required=True)
def file_diff(file1, file2, output):
    '''Compare two files and write the difference to an output file.'''
    ''' Example usage:  '''
    '''python diff_checker.py -f1 file1.txt -f2 file2.txt -o output.txt'''
    all_oa = []
    aws_oa = []
    with open(file1, "r") as file:
        for line in file:
            all_oa.append(line.strip())

    with open(file2, "r") as file:
        for line in file:
            aws_oa.append(line.strip())

    diff = list(set(all_oa)-set(aws_oa))
    diff.sort()

    with open(output, "a") as file:
        for token in diff:
            file.write(f'{token}\n')


if __name__=="__main__":
    file_diff()




