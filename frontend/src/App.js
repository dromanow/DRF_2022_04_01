import React from 'react'
import axios from 'axios'
import AuthorList from './components/AuthorList.js'
import BookList from './components/BookList.js'
import AuthorBookList from './components/AuthorBookList.js'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'


const NotFound = () => {
    var location = useLocation()

    return (
        <div>
            Page "{location.pathname}" not found
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': []
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                let authors = response.data
                this.setState({
                    'authors': authors
                })
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/books/')
            .then(response => {
                let books = response.data
                this.setState({
                    'books': books
                })
            })
            .catch(error => console.log(error))
    }
// http://localhost:3000/#/books
// http://localhost:3000/books
    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Authors</Link></li>
                        <li><Link to='/books'>Books</Link></li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element = {<AuthorList authors={this.state.authors} />} />
                        <Route exact path='/books' element = {<BookList books={this.state.books} />} />
                        <Route exact path='/authors' element = {<Navigate to='/' />} />
                        <Route exact path='/author/:id' element = {<AuthorBookList />} />
                        <Route path='*' element = {<NotFound />} />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
