def generate_section_HTML(concept_title, concept_description):
    html_text1 = '''
<div class="section">
    <div class="sectionTitle">
        ''' + concept_title
    html_text2 = '''
    </div>
    <div class="content">
        ''' + concept_description
    html_text3 = '''
    </div>
</div>'''
    
    full_html = html_text1 + html_text2 + html_text3
    return full_html

def get_title(lesson):
    start_location = lesson.find('TITLE:')
    end_location = lesson.find('CONTENT:')
    title = lesson[start_location+7 : end_location-1]
    return title

def get_description(lesson):
    start_location = lesson.find('CONTENT:')
    description = lesson[start_location+8 :]
    return description

def get_lesson_by_number(text, lesson_number):
    counter = 0
    while counter < lesson_number:
        counter = counter + 1
        next_lesson_start = text.find('TITLE:')
        next_lesson_end   = text.find('TITLE:', next_lesson_start + 1)
        if next_lesson_end >= 0:
            lesson = text[next_lesson_start:next_lesson_end]
        else:
            next_lesson_end = len(text)
            lesson = text[next_lesson_start:]
        text = text[next_lesson_end:]
    return lesson

TEST_TEXT = """TITLE: Computer Program
CONTENT: <p>
              Computers can be programed to do anything you need them to as long as you give them specific instructions on what needs to be done. You do this by giving me a precise sequence of steps that it can follow to do what you need it to do.
            </p>
            <p>
              <b>Terms used:</b><br>
              <ul>
                <li>computer
                <li>program
                <li>precise sequence of steps
                <li>computation
                <li>high-level launguage
                <li>input
                <li>interpreter</li>
              </ul>
            </p>
TITLE: Python & Python Expressions
CONTENT: Python is an interpreter that takes the written code and produces an output specific to the input or code written.  
Specific instructions need to be given in order for Python to be able to produce an output.  If there is something 
not clear (for example 2 + 2 +) then it does not have the ability to speculate what outcome your were looking for 
(like 2 + 2).
TITLE: Phython: Variables and Strings
CONTENT:    <p>
              In Python you use a = to assinge a value to a variable.  For example
              <span class="code">name="Danny"</span>.  This would make is so that <span class="code">print name</span> would then give you an output of <span class="code">Danny</span>.
            </p>
            <p>
              You can also use this to create something like this:<br>
              <span class="code">first="Danny "<br>
                last="McCormick"<br>
                print first + last<br>
              </span>
              This would then give you an outcome of <span class="code">Danny McCormick</span>
            </p>
TITLE: Differences in using Variables
CONTENT: On the other hand if you assign the variable a number value like number=2 
and then did print number + number you would get an outcome of 4. If
you put quote marks around the variable like a number, it is no longer considered a number. sonumber="2" and prnt number + number you would get an outcome of 22.
In Python saying somehting + something else does not always refer to acctual addition as in math, but adding/combining two Variables
depending on what the variables values are.
TITLE: Function?
CONTENT:           <p>
            What is a function in programing? A function takes an input and then produces an output.
          </p>
          <p>
            In order to write this in start with keyword <span class="code">def</span> followed by a function name and the function paramater in parentheses.
            What is in the parentheses will end being replaced by the actual value in the function when it is used.<br>
            For example if you wanted to square of a number you could write the following:<br>
          </p>
          <div class="codeblock">
            def square (x):<br>
              <span class="indent">answer = x * x</span><br>
              <span class="indent">return answer</span>
          </div>
          <p>
            In order to use this function we would write the name of the fuction folloed by the value we want to give it in parentheses.  like this:
          </p>
          <div class="codeblock">
            print square (4)<br>
            >>>16
          </div>
          <p>
            If there is does not have a return statement the you will get a result of <span class="code">None</span>.  Here is an example of what that would look like:
          </p>
          <div class="codeblock">
            def add two(x):<br>
            <span class="indent">answer = x + 2</span>
            <br><br>
            new_number = add_two (7)<br>
            print new_number<br>
            >>>None
          </div>
          <p>
            <b> Retrun vs Print:</b> Without a 'return' statement the code really isn't doing anything even though it may print something out in text.  To make a function whole and complete you should end with a return statement.
          </p>
TITLE: When and how are they used?
CONTENT: An if statement is used to determine which set of codes is to be used. For example if x = 5
then multiply by 10, else mulitply by 2. While loops on the other hand repeart until a criteria/condition is met.
For example while the date is less than 15 add $2 to x.  The code will continue until the date is no longer less than 15 and will continue to perform the function of adding $2.
          <ul>
            <li><b>== (equals), != (doen't equal), >, <, >=, <=:</b> Are all Python comparison operations that would return a bolean value of True or False depending if the expression was true or not. For example, 10 != 100 would return a
            True since 10 does not equal 100.
            <li><b>if, then, else:</b> These would be used when you wanted to execute different operations
            depending on what the requirements were. For example if it's a weekday you want to charge $5, but on weekends you want to charge $10 you can use an if statement.
            <li><b>while loops:</b> This is used to repeat a function until that specific criteria is met, at which point you would stop. So while count is less than 100 execute count = count + 5 and this will continue until the condition is met. 
            </li>
          </ul>
TITLE: How to Solve Problems
CONTENT: There are two key components when it comes to solving problems: <b>input</b> and <b>output</b>. Understanding the inputs and outputs of anything will help you better underdtand how it works and resolve any potention problem.  This is the same for coding and if you come accross any issue executing the code.
          <ul>
            <li><b>Inputs:</b> Understanding the inputs that make up a code will help you better understand how to resolve if any issues happen on execution.
            <li><b>Outputs:</b> If you know what your code is actually suppose to do or your what your output should be, this will help if executing it has issues.</li>
          </ul>
            Knowing and understanding your inputs and outputs of any code are key to help determine any potential issue when the code does not work as expected."""


def generate_all_html(text):
    current_lesson_number = 1
    lesson = get_lesson_by_number(text, current_lesson_number)
    all_html = ''
    while lesson != '':
        title = get_title(lesson)
        description = get_description(lesson)
        lesson_html = generate_section_HTML(title, description)
        all_html = all_html + lesson_html
        current_lesson_number = current_lesson_number + 1
        lesson = get_lesson_by_number(text, current_lesson_number)
    return all_html


print generate_all_html(TEST_TEXT)