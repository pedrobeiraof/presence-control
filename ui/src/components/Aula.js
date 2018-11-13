import React, { Component } from 'react';
import axios from 'axios'
import Camera from 'react-camera';
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
    this.fetchAlunos()
    this.countdown = setInterval(() => this.reconhecerAlunos(), 3000);
  }

  componentWillUnmount() {
    clearInterval(this.countdown);
  }

  reconhecerAlunos() {
    const { params } = this.props.match
    this.camera.capture()
    .then(blob => {
      var data = new FormData();
      data.append('imagem', blob);
      data.append('id_aula', params.id);
      axios.post(`http://localhost:8000/recognition/`, data)
        .then(response => {
          console.log(response)
          this.setState({ alunosPresentes: response.data })
        })
        .catch(error => {
          console.log(error)
        })
    })
  }

  fetchAlunos() {
  	const { params } = this.props.match
    axios.get(`http://localhost:8000/aulas/${params.id}`)
      .then(response => {
        this.setState({ alunos: response.data.alunos })
      })
      .catch(error => {
        console.log(error)
      })
  }

  render() {
    const { alunos, alunosPresentes } = this.state;
    const columns = [{
			Header: 'Nome',
			accessor: 'nome'
    }, {
			Header: 'RA',
			accessor: 'ra'
    }, {
      id: 'alunosPresentes',
      Header: 'Status',
      accessor: d => alunosPresentes.indexOf(d.id) === -1 ? 'Ausente' : 'Presente'
    }]

    return (
      <div className="list-base">
        <ReactTable
          data={alunos}
          columns={columns}
        />
        <div hidden>
          <Camera
            ref={(cam) => {
              this.camera = cam;
            }}
          />
        </div>
      </div>
    );
  }
}

export default Aula;
