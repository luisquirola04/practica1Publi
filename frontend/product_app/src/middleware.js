import { NextResponse } from 'next/server';
import axios from 'axios';

async function validar(token) {
    const url = 'http://localhost:5000/validar/Token';
    try {
        console.log(`Enviando token: ${token}`);  // Log para verificar que el token se está enviando

        const response = await axios.get(url, {
            headers: {
                'X-Access-Token': token.value,
                'Content-Type': 'application/json'
            }
        });

        console.log('Respuesta de validación:', response.data);  // Log para verificar la respuesta
        return response.data;
    } catch (error) {
        console.error('Error validando el token:', error);
        return { code: 500, message: 'Error de servidor' };
    }
}
export default async function middleware(request) {
    console.log('ESTOY EN EL MIDDLEWARE');

    const token = request.cookies.get('token');
    console.log('Token:', token);  // Log para verificar el token
    
    if (!token) {
        console.log("Token no encontrado, redirigiendo a sesión");
        const nextResponse = NextResponse.redirect('http://localhost:3000/sesion');
        return nextResponse;
    }

    const validation = await validar(token);
    console.log('Validación:', validation);  // Log para verificar la respuesta de validación

    if (validation.code != 200) {
        console.log("Token inválido o error en validación, redirigiendo a sesión");
        const nextResponse = NextResponse.redirect('http://localhost:3000/sesion');
        request.cookies.remove('token')
        request.cookies.remove('user')

        
        return nextResponse;
    }

    return NextResponse.next();
}

export const config = {
    matcher: [
        '/product',
        '/account',
        '/batch',
        '/components',
    ]
};
