from cassandra.cluster import Cluster
import flask
#from flask import Flask
from flask import jsonify, render_template, request
import json

app = flask.Flask(__name__) 

#@app.route("/")
#@app.route("/real/")  
#def hello(): 
#    return "StID, Car Count" 


@app.route("/real/")
def cassandra_test1():
	cluster = Cluster(['54.175.15.242'])
        session = cluster.connect()
	session.set_keyspace("keyspace_realtime")
	rows = session.execute("SELECT * FROM mytable")
	streets = []
	def inner():
		yield 'StID, &nbsp;&nbsp;&nbsp;&nbsp;Car Count<br/>\n'
		for row in rows:
			#streets.append({'counter': row[0].split('key')[1], 'id': row[1].split('\''), 'cc': row[2].split('\'')})
			#streets.append({'id': row[1].split('\''), 'cc': row[2].split('\'')})
			#print row[0]
			outputstr = row[1].split('\'')[0] + ', ' + row[2].split('\'')[0]
			yield '%s<br/>\n' % outputstr
        #return jsonify(streets=streets)
	return flask.Response(inner(), mimetype='text/html')
	#return render_template('topicBycity.html',data =row[0])


@app.route("/batch/")
def cassandra_test2():
        cluster = Cluster(['54.175.15.242'])
        session = cluster.connect()
        session.set_keyspace("keyspace_batch")
        rows = session.execute("SELECT * FROM mytable")
	if rows is None:
		print "none"
	streets = []
        def inner():
                yield 'StID, &nbsp;&nbsp;&nbsp;&nbsp;Car Count<br/>\n'
                for row in rows:
                        #streets.append({'counter': row[0].split('key')[1], 'id': row[1].split('\''), 'cc': row[2].split('\'')})
                        #streets.append({'id': row[1].split('\''), 'cc': row[2].split('\'')})
                        #print row[0]
                        outputstr = row[1].split('\'')[0] + ', ' + row[2].split('\'')[0]
                        yield '%s<br/>\n' % outputstr
        #return jsonify(streets=streets)
        return flask.Response(inner(), mimetype='text/html')
        #return render_template('topicBycity.html',data =row[0])

@app.route("/batch_test/")
def cassandra_test3():
        cluster = Cluster(['54.175.15.242'])
        session = cluster.connect()
        session.set_keyspace("keyspace_batch")
        rows = session.execute("SELECT * FROM mytable_rdd")
        if rows is None:
                print "none"
        streets = []
        def inner():
                yield 'StID, &nbsp;&nbsp;&nbsp;&nbsp;Car Count<br/>\n'
                for row in rows:
                        outputstr = row[0].split('\'')[0] + ', ' + row[1].split('\'')[0]
                        yield '%s<br/>\n' % outputstr
        return flask.Response(inner(), mimetype='text/html')


if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)
