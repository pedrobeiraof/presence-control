import React, { Component } from 'react';
import axios from 'axios'
import ReactTable from "react-table";

class Aula extends Component {
  constructor(props) {
    super(props);
    this.state = {
      alunos: [],
      alunosPresentes: [],
    }
  }
  componentDidMount() {
    this.fetchRelatorio()
  }

  fetchRelatorio() {
  	const { params } = this.props.match
  	const config = {
  		params: {
  			aula_id: params.id,
  		}
  	}
    axios.get('http://localhost:8000/relatorio', config)
      .then(response => {
        this.setState({ alunos: response.data })
      })
      .catch(error => {
        console.log(error)
      })
  }

  render() {
    const { alunos, alunosPresentes } = this.state;
    const columns = [{
		Header: 'Aluno',
		accessor: 'aluno'
    }, {
		Header: 'Presença(%)',
		accessor: 'porcentagem'
    }, {
      id: 'alunosPresentes',
      Header: 'Status',
      accessor: d => d.presente ? 'Presente' : 'Ausente'
    }]

    return (
	    <div className="list-base">
	      <h1>Alunos</h1>
	      <ReactTable
	        data={alunos}
	        columns={columns}
	      />
	    </div>
    );
  }
}

export default Aula;
