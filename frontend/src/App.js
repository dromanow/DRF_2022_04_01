import React from 'react'
import axios from 'axios'
import AuthorList from './components/AuthorList.js'
import BookList from './components/BookList.js'
import BookForm from './components/BookForm.js'
import AuthorBookList from './components/AuthorBookList.js'
import LoginForm from './components/LoginForm.js'
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
            'books': [],
            'token': ''
        }
    }

    obtainAuthToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {"username": login, "password": password})
            .then(response => {
                let token = response.data.token
                console.log(token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/authors/', {headers})
            .then(response => {
                let authors = response.data
                this.setState({
                    'authors': authors
                })
            })
            .catch(error => {
                this.setState({
                    'authors': []
                })
                console.log(error)
            })

        axios
            .get('http://127.0.0.1:8000/api/books/', {headers})
            .then(response => {
                let books = response.data
                this.setState({
                    'books': books
                })
            })
            .catch(error => {
                this.setState({
                    'books': []
                })
                console.log(error)
            })
    }

    createBook(title, authors) {
        let headers = this.getHeaders()

        axios
            .post('http://127.0.0.1:8000/api/books/', {'title': title, 'authors': authors}, {headers})
            .then(response => {
                this.getData()
            })
            .catch(error => {
                console.log(error)
            })

    }

    deleteBook(id) {
        let headers = this.getHeaders()

        axios
            .delete(`http://127.0.0.1:8000/api/books/${id}`, {headers})
            .then(response => {
                let books = response.data
                this.setState({
                    'books': this.state.books.filter((book) => book.id != id)
                })
            })
            .catch(error => {
                console.log(error)
            })
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Authors</Link></li>
                        <li><Link to='/books'>Books</Link></li>
                        <li><Link to='/books/create'>New book</Link></li>
                        <li>
                        { this.isAuth() ? <button onClick={()=>this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                        </li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element = {<AuthorList authors={this.state.authors} />} />
                        <Route exact path='/books' element = {<BookList books={this.state.books} authors={this.state.authors} deleteBook={(id) => this.deleteBook(id)} />} />
                        <Route exact path='/books/create' element = {<BookForm authors={this.state.authors} createBook={(title, authors) => this.createBook(title, authors)} />} />
                        <Route exact path='/login' element = {<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)}/>} />
                        <Route exact path='/authors' element = {<Navigate to='/' />} />
                        <Route exact path='/author/:id' element = {<AuthorBookList books={this.state.books} />} />
                        <Route path='*' element = {<NotFound />} />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
