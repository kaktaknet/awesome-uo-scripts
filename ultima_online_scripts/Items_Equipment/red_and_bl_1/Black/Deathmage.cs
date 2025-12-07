using System;
using System.Collections;
using Server.Items;
using Server.Targeting;

namespace Server.Mobiles
{
	[CorpseName( "a wizard's body" )]
	public class Deathmage : BaseCreature
	{
		public override bool ShowFameTitle{ get{ return false; } }
		
		[Constructable]
		public Deathmage() : base( AIType.AI_Mage, FightMode.Closest, 10, 1, 0.2, 0.4 )

		{			
			SpeechHue = Utility.RandomDyedHue(); 
			Name = "a death mage";  
			Body = 0x190; 

 	   		 // *Begin* //
   	   		Item HoodedShroudofShadows = new HoodedShroudOfShadows();
      
         		HoodedShroudofShadows.Hue = 2406;
        		 HoodedShroudofShadows.Movable = false;

        		 AddItem( HoodedShroudofShadows );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item boots = new Boots();
      
         		boots.Hue = 2406;
        		 boots.Movable = false;

        		 AddItem( boots );
        		 // *End* //

 	   		 // *Begin* //
   	   		Item leathergloves = new LeatherGloves();
      
         		leathergloves.Hue = 2406;
        		 leathergloves.Movable = false;

        		 AddItem( leathergloves );
        		 // *End* //
         
			SetStr( 75, 80 );
			SetDex( 90, 105 );
			SetInt( 160, 200 );
			SetHits( 150, 190 );

			SetDamage( 11, 15 );

			SetSkill( SkillName.MagicResist, 90.0, 100.0 );
			SetSkill( SkillName.EvalInt, 95.0, 100.0 );
			SetSkill( SkillName.Magery, 95.0, 100.0 );
			SetSkill( SkillName.Wrestling, 75.0, 80.0 );
			SetSkill( SkillName.Anatomy, 75.0, 80.0 );

			Fame = 10000;
			Karma = -7500;

			VirtualArmor = 40;

			Item hair = new Item( Utility.RandomList( 0x203B, 0x2049, 0x2048, 0x204A ) );
			hair.Hue = Utility.RandomNondyedHue();
			hair.Layer = Layer.Hair;
			hair.Movable = false;
			AddItem( hair );

			

		}

		public override void GenerateLoot()
		{
			AddLoot( LootPack.FilthyRich );
			AddLoot( LootPack.LowScrolls );
		}
		
		public override bool AlwaysMurderer{ get{ return true; } }

		public Deathmage( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}
