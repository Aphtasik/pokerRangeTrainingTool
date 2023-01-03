import '../styles/navbar.css'
import { Link, useMatch, useResolvedPath } from 'react-router-dom'

export default function Navbar() {
    return (
        <nav className="navbar" id="myNavbar">
            <CustomLink to="/my-ranges">My Ranges</CustomLink>
            <CustomLink to="/train-ranges">Train Ranges</CustomLink>
            <CustomLink to="/train-hands">Train Hands</CustomLink>
        </nav>
    )
}

function CustomLink({ to, children, ...props }) {
    const resolvedPath = useResolvedPath(to)
    const isActive = useMatch({ path: resolvedPath.pathname , end: true })

    return (
        <Link className={isActive ? "active" : ""} to={to} {...props}>
            {children}
        </Link>
    )
}