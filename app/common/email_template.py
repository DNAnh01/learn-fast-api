def email_verify_template(user_name: str, redirect_url: str, mode: int) -> str:
    if mode == 1:
        button_text = "Go to Landing Page"
        button_style = "background-color: #2c2c2c; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 5px; font-size: 16px;"
        button_link = redirect_url
    elif mode == 2:
        button_text = "Verify Email"
        button_style = "background-color: #2c2c2c; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 5px; font-size: 16px;"
        button_link = redirect_url
    return f"""
            <!DOCTYPE html>
                <html lang="en">

                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Verify Email Address for Ally AI</title>
                </head>

                <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #eff2f4;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
                        <tr>
                            <td align="center">
                                <img src="https://raw.githubusercontent.com/DNAnh01/assets/main/ally-ai-logo.png"
                                    alt="Ally AI Logo" style="display: block; width: 200px; margin: 20px auto;">
                            </td>
                        </tr>
                        <tr>
                            <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;">
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td style="color: #153643; font-size: 28px;">
                                            <b>Hey {user_name},</b>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 20px 0 30px 0; color: #153643; font-size: 16px; line-height: 20px;">
                                            Thanks for registering for an account on Ally AI! Before we get started, we just need to
                                            confirm that this is you. Click below to verify your email address:
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="text-align: center;">
                                            <a href="{button_link}" style="{button_style}">{button_text}</a>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td bgcolor="#ffffff" style="padding: 30px 30px 30px 30px;">
                                <hr>
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td style="color: #153643; font-size: 14px; text-align: center;">
                                            Term of Service | Privacy Statement
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </body>

                </html>
            """


def email_forgot_password_template(user_name: str, password_reset: str) -> str:
    return f"""
            <!DOCTYPE html>
                <html lang="en">

                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Reset Password for Ally AI</title>
                </head>

                <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #eff2f4;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
                        <tr>
                            <td align="center">
                                <img src="https://raw.githubusercontent.com/DNAnh01/assets/main/ally-ai-logo.png" alt="Ally AI Logo"
                                    style="display: block; width: 200px; margin: 20px auto;">
                            </td>
                        </tr>
                        <tr>
                            <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;">
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td style="color: #153643; font-size: 28px;">
                                            <b>Hey {user_name},</b>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 20px 0 30px 0; color: #153643; font-size: 16px; line-height: 20px;">
                                            We received a request to reset your password. Please follow the instructions below to reset
                                            your password:
                                        </td>
                                    </tr>
                                    <tr>
                                        <td
                                            style="padding: 20px 0 30px 0; color: #153643; font-size: 20px; line-height: 20px; text-align: center; font-weight: 600; display: flex; justify-content: center; align-items: center;">
                                            <div
                                                style="background-color: #eff2f4; border: 2px solid #2c2c2c; padding: 10px; border-radius: 5px; width: 40%; display: flex; justify-content: center; align-items: center;">
                                                {password_reset}
                                            </div>
                                        </td>
                                    </tr>

                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td bgcolor="#ffffff" style="padding: 30px 30px 30px 30px;">
                                <hr>
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td style="color: #153643; font-size: 14px; text-align: center;">
                                            Term of Service | Privacy Statement
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </body>

                </html>
            """
