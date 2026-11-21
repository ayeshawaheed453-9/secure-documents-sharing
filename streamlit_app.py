                        "⬇ Download Encrypted Package",
                        data=package,
                        file_name=uploaded_file.name + ".sdsp",
                        mime="application/octet-stream",
                        type="primary",
                        use_container_width=True
                    )

                except core.SDSPError as e:
                    st.error(f"[{e.status}] {e}")

                except Exception:
                    st.error("Encryption failed. Verify your files.")


# ==========================================
# DECRYPT FILE
# ==========================================

with tab_decrypt:

    st.markdown("""
    <div class="page-intro">
        <div class="page-icon">🔓</div>
        <div>
            <h2>Decrypt Your Document</h2>
            <p>Recover your original document using your private key.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        st.markdown("#### Step 1 — Upload Encrypted Package")

        encrypted_file = st.file_uploader(
            "Select encrypted package (.sdsp)",
            key="pkg"
        )

        if encrypted_file:
            st.success(f"Package selected: {encrypted_file.name}")

        st.divider()

        st.markdown("#### Step 2 — Upload Your Private Key")

        private_key_file = st.file_uploader(
            "Select your private key (.pem)",
            type=["pem"],
            key="priv"
        )

        if private_key_file:
            st.success("Private key uploaded.")

        password2 = st.text_input(
            "Private key passphrase",
            type="password",
            key="pw2",
            placeholder="Enter your private key passphrase"
        )

        st.divider()

        if st.button(
            "🔓 Decrypt Document",
            type="primary",
            use_container_width=True
        ):

            if not encrypted_file or not private_key_file:
                st.warning("Please upload both required files.")

            else:
                try:
                    with st.spinner("Verifying and decrypting..."):

                        data, original_name = core.decrypt_bytes(
                            encrypted_file.getvalue(),
                            private_key_file.getvalue(),
                            password2.encode() or None
                        )

                    st.success(
                        "Authenticity verified. Decryption successful!"
                    )

                    st.markdown("""
                    <div class="success-panel">
                        <div class="success-icon">✓</div>
                        <div>
                            <h3>Decryption Complete</h3>
                            <p>Your original document is ready to download.</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.download_button(
                        "⬇ Download Original Document",
                        data=data,
                        file_name=original_name or "decrypted_file",
                        mime="application/octet-stream",
                        type="primary",
                        use_container_width=True
                    )

                except core.SDSPError as e:
                    st.error(f"[{e.status}] {e}")

                except Exception:
                    st.error(
                        "Decryption failed. Check your key and passphrase."
                    )


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    <div class="footer-brand">🔐 SecureVault</div>
    <p>Secure Document Sharing System</p>
    <p>Built with Python · Streamlit · Cryptography</p>
    <div class="footer-line"></div>
    <small>Educational Prototype | Protect your digital documents.</small>
</div>
