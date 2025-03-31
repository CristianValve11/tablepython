from flask import Flask,render_template,request


app=Flask('Tabla de multiplicar')

@app.route('/',methods=['GET'])
def formulario():
    return render_template('formulario.html')

    
@app.route('/tabla',methods=['GET','POST'])
def tabla():
    if request.method=="POST":
        num=int(request.form.get('num'))
        return render_template("mostrardatos.html",num=num)
    elif request.method=="GET":
        return render_template("error.html")

@app.errorhandler(404)
def bar(error):
    return render_template('error.html'), 404

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0') #todas las ip de mi ordenador



