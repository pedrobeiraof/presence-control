import React, { Component } from 'react';
import axios from 'axios'
import ReactTable from "react-table";
import { Link } from "react-router-dom";

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
    console.log(Date.now())
    console.log(d.original.data_final)
    return <Link to={`/aulas/${d.original.id}`}>AQUI</Link>
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
      <div>
        <ReactTable
          data={aulas}
          columns={columns}
        />
      </div>
    );
  }
}

export default ListAulas;
