import click
import driver.web

@click.group()
def tipper():
    pass

@tipper.command()
def cmd1():
    '''Command on src'''
    click.echo('src cmd1')

@tipper.command()
def cmd2():
    '''Command on src'''
    click.echo('src cmd2')

if __name__ == '__main__':
    driver.web.initialTest()
