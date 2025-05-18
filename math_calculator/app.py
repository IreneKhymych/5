from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
import os
import json
import xml.etree.ElementTree as ET
from werkzeug.utils import secure_filename
from utils.math_ops import basic_operations, solve_equation
from utils.stats import compute_statistics
from utils.plotter import plot_function

folder = 'uploads'
extentions = {'json', 'xml'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = folder
app.secret_key = 'secret_key'
os.makedirs(folder, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extentions

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'taskfile' not in request.files:
        flash('Завантажте файл завдання.')
        return redirect(url_for('index'))
    task_file = request.files['taskfile']
    if not (task_file and allowed_file(task_file.filename)):
        flash('Неправильний формат файлу завдання (допустимо: .json, .xml).')
        return redirect(url_for('index'))

    if 'datafile' not in request.files:
        flash('Завантажте файл з даними.')
        return redirect(url_for('index'))
    data_file = request.files['datafile']
    if not data_file:
        flash('Файл з даними не завантажено.')
        return redirect(url_for('index'))

    task_filename = secure_filename(task_file.filename)
    task_path = os.path.join(app.config['UPLOAD_FOLDER'], task_filename)
    task_file.save(task_path)

    data_filename = secure_filename(data_file.filename)
    data_path = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
    data_file.save(data_path)

    result = task_with_data(task_path, data_path)
    return render_template('result.html', result=result)

def parse_file(filepath):
    if filepath.endswith('.json'):
        with open(filepath, encoding='utf-8') as f:
            return json.load(f)
    elif filepath.endswith('.xml'):
        tree = ET.parse(filepath)
        root = tree.getroot()

        def to_dict(elem):
            result = {}
            for child in elem:
                if list(child):
                    result[child.tag] = to_dict(child)
                else:
                    result[child.tag] = child.text
            return result

        return {root.tag: to_dict(root)}
    else:
        raise ValueError("Непідтримуваний формат файлу")

def task_with_data(task_path, data_path):
    try:
        task = parse_file(task_path)
        task = task.get('task', task)
    except Exception as e:
        return f'Помилка при обробці файлу завдання: {e}'

    try:
        with open(data_path, encoding='utf-8') as f:
            data_lines = f.read().strip().splitlines()

        if task.get('operation') == 'arithmetic':
            if len(data_lines) != 3:
                return "Очікується формат даних: число1, операція, число 2 (кожне на новому рядку)"
            a = float(data_lines[0])
            op = data_lines[1]
            b = float(data_lines[2])
            result = basic_operations(a, b, op)
            return f"<b>Операція:</b> {a} {op} {b} = <b>{result}</b>"

        if 'stats' in task or task.get('operation') == 'statistics':
            nums = [float(x) for x in data_lines]
            stats = compute_statistics(nums)
            return "<b>Статистика з файлу даних:</b><br>" + "<br>".join(f"{k}: {v}" for k, v in stats.items())

        if 'plot' in task or task.get('operation') == 'plot':
            x_range = [float(x) for x in data_lines]
            expr = task.get('function') or task['plot']['expr']
            img_path = plot_function(expr, x_range, app.config['UPLOAD_FOLDER'])
            img_name = os.path.basename(img_path)
            return f'<b>Графік функції:</b><br><img src="{url_for("uploaded_file", filename=img_name)}" alt="plot">'

        if 'op' in task:
            nums = [float(x) for x in data_lines]
            a, b = nums[0], nums[1]
            op = task['op']
            result = basic_operations(a, b, op)
            return f"<b>Операція:</b> {a} {task['op']} {b} = <b>{result}</b>"

        if 'equation' in task or task.get('operation') == 'linear_equation':
            coeffs = [float(x) for x in data_lines]
            eq_type = "лінійне" if task.get('operation') == "linear_equation" else task.get('equation') or task['equation']
            result = solve_equation(eq_type, coeffs)
            return f"<b>Розв'язок рівняння {eq_type} </b> {result}"

        return "Невідома задача або формат даних."

    except Exception as e:
        return f'Помилка обчислення: {e}'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)