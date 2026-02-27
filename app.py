# 5. LLM Logic - Improved for detailed steps
    if api_key and st.button("✨ Generate Step-by-Step Upcycling Guide"):
        try:
            client = openai.OpenAI(api_key=api_key)
            
            # We are telling the AI exactly how to format the answer
            prompt = (
                f"The camera detected: {detected_str}. "
                "Act as an expert Upcycling Assistant. For these items, provide 3 detailed DIY projects. "
                "For each project, you MUST include: "
                "1. A catchy Project Title. "
                "2. A list of 'Extra Materials' needed (like glue, scissors, paint). "
                "3. A clear, numbered 'Step-by-Step Process' so a beginner can follow it. "
                "Keep the tone encouraging and eco-friendly!"
            )
            
            with st.spinner("🧠 Brainstorming creative steps for you..."):
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}]
                )
                
                # Display the result in a nice format
                st.divider()
                st.subheader("🛠️ Your Upcycling Roadmap")
                st.markdown(response.choices[0].message.content)
                
        except Exception as e:
            st.error(f"Error: {e}. Please check your API key and billing balance.")
