import React, { Component } from 'react';
import axios from 'axios'
import ReactTable from "react-table";
import { Link } from "react-router-dom";
import 'react-table/react-table.css'

class ListAulas extends Component {
  constructor(props) {
    super(props);
    this.state = {
      aulas: []
    }
  }
  componentDidMount() {
    this.fetchAulas()
  }

  fetchAulas() {
    axios.get('http://localhost:8000/aulas')
      .then(response => {
        console.log(response.data)
        this.setState({ aulas: response.data })
      })
      .catch(error => {
        console.log(error)
      })
  }

  handleLink(d) {
    if (d.original.tipo === 2) {
      return <Link to={`/aulas/${d.original.id}`}>AQUI</Link>
    }
    if (d.original.tipo === 3) {
      return <Link to={`/relatorios/${d.original.id}`}>AQUI</Link> 
    }
    return null
  }

  render() {
    const { aulas } = this.state;
    const columns = [{
      Header: 'Nome',
      accessor: 'ds_aula'
    }, {
      Header: 'Inicio',
      accessor: 'data_inicio'
    }, {
      Header: 'Final',
      accessor: 'data_final'
    }, {
      Header: 'Acessar',
      Cell: d => this.handleLink(d)
    }]

    return (
      <div className="list-base">
        <h1>Aulas</h1>
        <ReactTable
          data={aulas}
          columns={columns}
        />
      </div>
    );
  }
}

export default ListAulas;
